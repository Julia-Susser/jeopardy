let message = document.getElementById("final")
const param = new URLSearchParams(window.location.search)
let quest_answer = '"'+param+'"'

let your_answer = quest_answer.split("=")[1].replace('"', '').split("+")
your_answer = your_answer.join(" ")
let number = quest_answer.split("=")[0]+'"'
let show_num = number.split("%2F")[0].replace('"', '')
let quest_num = number.split("%2F")[1].replace('"', '')
let answer = ShowsJSON.shows[show_num].questions[quest_num].answer
let value = ShowsJSON.shows[show_num].questions[quest_num].value
if (your_answer.toLowerCase() === answer.toLowerCase()){
  message.innerHTML = "You Won. You earned $" + value + "."
}else{
  message.innerHTML = "You Lost. You lost the opportunity to get $" + value + "."
}

let review = document.getElementById('review')
review.innerHTML = "Your Answer: " + your_answer
document.body.appendChild(review)

let ans = document.createElement('p')
ans.innerHTML = " Real Answer: " + answer
document.body.appendChild(ans)
