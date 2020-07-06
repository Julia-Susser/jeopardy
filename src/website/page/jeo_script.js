

let el = document.createElement('p')
el.innerHTML = "Date: " + date +",\n Value: $" + value + ", Category: " + category.toLowerCase()
document.body.appendChild(el)

document.write('<form action="../submit/jeo-submit.html" method="GET" id="formey">')

document.write('<label for="quest"><h3> '+question+': </h3> </label>')
name_id = num + "/" + num2
document.write('<input id="quest" type="text" name="'+name_id+'">')
document.write('</form>')




let butt = document.createElement("BUTTON");
butt.id = "hint"
butt.innerHTML = "Hint";
document.body.appendChild(butt);


let ans = document.createElement('p');
ans.id = "ansey";
let first_letter = answer[0]
ans.innerHTML = "First Letter: " + first_letter;
document.body.appendChild(ans);


hint = document.getElementById("hint")
ansey = document.getElementById("ansey")


hint.onmouseover = function(){
  ansey.style.display = 'block'
}
document.onmouseout = function(){
  el.innerHTML = "BYE!"
}
document.onmouseover = function(){
  el.innerHTML = "Date: " + date +",\n Value: $" + value + ", Category: " + category.toLowerCase()
}

let ann = function(){
  ansey.style.display = 'none'
}
hint.onmouseout = ann
