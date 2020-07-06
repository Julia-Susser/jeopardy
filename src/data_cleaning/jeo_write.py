import sqlite3


conn = sqlite3.connect('../../output/jeopardy.sqlite')
cur = conn.cursor()

cur.execute("""SELECT questions.question, questions.answer, val.value, dates.date, dates.show_num, categorys.category
FROM questions JOIN val JOIN dates JOIN categorys
WHERE questions.date_id = dates.id AND questions.category_id = categorys.id AND questions.value_id IS NOT NULL AND questions.value_id = val.id
ORDER BY dates.date DESC""")
dates = []

with open ("../../output/jeopardy.js", "w") as jeo:
    jeo.write("const ShowsJSON = {shows : [\n")
    for row in cur:
        question = row[0]
        answer = row[1]
        value = row[2]
        date = row[3]
        show_num = row[4]
        category= row[5]

        if len(dates) == 0:
            dates.append(date)
            jeo.write('{\ndate : "' + date + '",')
            jeo.write('\nshow_num : "' + show_num + '",')
            jeo.write('\nquestions : [\n{\nquestion : "'+ question +'",\nanswer : "'+ answer +'",\nvalue : "'+ value +'",\ncategory : "'+category+'"\n}')
        elif date not in dates:
            jeo.write("]\n},\n")
            dates.append(date)
            jeo.write('{\ndate : "' + date + '",')
            jeo.write('\nshow_num : "' + show_num + '",')
            jeo.write('\nquestions : [\n{\nquestion : "'+ question +'",\nanswer : "'+ answer +'",\nvalue : "'+ value +'",\ncategory : "'+category+'"\n}')
        else:
            jeo.write(",")
            jeo.write('\n{\nquestion : "'+ question +'",\nanswer : "'+ answer +'",\nvalue : "'+ value +'",\ncategory : "'+category+'"\n}')
    jeo.write("\n]\n}\n]\n}")
