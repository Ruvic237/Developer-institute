// JS External file

//getting the div element
let show = document.getElementById("container").innerHTML;
console.log(show);

//getting the lastElementChild
let change = document.getElementsByClassName("list")[0].lastElementChild;
change.innerHTML="Richard";
console.log(change.innerHTML);

//getting all first child of each parent ul
let change1 = document.querySelectorAll("ul>li:first-child");
for(let x of change1 ){
	x.innerHTML="Ruvic";
}

//calling li element to remove sarah 
let change2 = document.getElementsByTagName("li");

for(let i=0;i<change2.length;i++){
	if(change2[i].innerHTML == "Sarah"){
		change2[i].style.display="none";
	}
}



