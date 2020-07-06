import json
import sqlite3
import re
import time
from datetime import datetime
conn = sqlite3.connect('../../output/jeopardy.sqlite')
cur = conn.cursor()
def how_many(limit):
    num = input("How many different jeopardy questions do you want to read? LIMIT is {}.\n".format(limit))
    if len(num) <= 0:
        num = limit
    try:
        if int(num) < 1 or int(num) > limit:
            print("not valid. we will extract 2000 rows")
            num = 2000
        return int(num)
    except ValueError:
        print("not valid input. we will extract 2000 rows")
        return 2000

def new_tables():
    cur.executescript(
    """
    DROP TABLE IF EXISTS questions;
    DROP TABLE IF EXISTS dates;
    DROP TABLE IF EXISTS categorys;
    DROP TABLE IF EXISTS val;
    CREATE TABLE IF NOT EXISTS questions(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        question TEXT UNIQUE,
        answer TEXT UNIQUE,
        date_id INTEGER,
        value_id INTEGER,
        category_id INTEGER

    );
    CREATE TABLE IF NOT EXISTS val(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        value TEXT UNIQUE
    );

    CREATE TABLE IF NOT EXISTS categorys(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        category TEXT UNIQUE
    );
    CREATE TABLE dates(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        date TEXT UNIQUE,
        show_num TEXT UNIQUE
    )

    """

    )
    conn.commit()

def get_data(quest, count):
    question = quest["question"].strip("''")
    ans = quest["answer"]
    date = quest["air_date"]
    num = quest["show_number"]
    category = quest["category"]


    date = datetime.strptime(date, "%Y-%m-%d")
    date = datetime.strftime(date, "%b %d, %Y")
    qs1 = question.split("</a>")
    question2 = " ".join(qs1)
    regular_ex = re.findall('<a href=.+?>', question2)
    for x in regular_ex:
        qs2 = question2.split(x)
        question = " ".join(qs2)


    rex = re.findall('<a href=.+?>', question)
    for x in rex:
        qs3 = question.split(x)
        question = " ".join(qs3)

    question = question.replace('"', "'")
    ans = ans.replace('"', "'")
    cs = category.split('"')
    category = "'".join(cs)

    try:
         value = quest["value"].strip("$")
    except AttributeError:
        value = quest["value"]
    print("row ".upper() + str(count + 1))
    print("Category:", category)
    print("Question:", question)
    print("Answer:", ans)
    print("Date:", date)
    print("Show Number:", num)
    print("\n\n")

    return question, ans, date, num, category, value

def enter_everything(question, ans, date, num, category, value):
    cur.execute("""INSERT OR IGNORE INTO dates(date, show_num) VALUES(?, ?)""", (date, num))
    cur.execute(
    """SELECT id FROM dates WHERE date = ? AND show_num = ?""", (date, num)
    )
    try:
        date_id = cur.fetchone()[0]
    except:
        print("Could not get id!")
        pass
    cur.execute("""INSERT OR IGNORE INTO categorys(category) VALUES(?)""", (category,))
    cur.execute(
    """SELECT id FROM categorys WHERE category = ?""", (category,)
    )
    try:
        category_id = cur.fetchone()[0]
    except:
        print("Could not get id!")
        pass
    if value != None:
        cur.execute("""INSERT OR IGNORE INTO val(value) VALUES(?)""", (value,))
        cur.execute(
        """SELECT id FROM val WHERE value = ?""", (value,)
        )
        try:
            v_id = cur.fetchone()[0]
        except:
            print("Could not get id!")
            return None
        cur.execute("""INSERT OR IGNORE INTO questions(question, answer, date_id, value_id, category_id) VALUES(?, ?, ?, ?, ?)""", (question, ans, date_id, v_id, category_id))

    else:
        cur.execute("""INSERT OR IGNORE INTO questions(question, answer, date_id, category_id) VALUES(?, ?, ?, ?)""", (question, ans, date_id, category_id))
        #time.sleep(1)

with open("../../input/JEOPARDY_QUESTIONS1.json") as jeo:
    jeop = jeo.read()
    file = json.loads(jeop)
    limit = len(file)
    times = how_many(limit)
    count = 0
    date_num = {}
    new_tables()
    for quest in file:
        if count == times:
            break
        if count == 100:
            conn.commit()
        question, ans, date, num, category, value = get_data(quest, count)
        enter_everything(question, ans, date, num, category, value)
        count += 1


conn.commit()
