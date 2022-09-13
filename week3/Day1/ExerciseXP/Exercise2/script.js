// js external file

//getting div element to style
let ne = document.querySelector("div");
ne.style.color = "blue";
ne.style.padding = "90px";

//getting the element containing John
let geting = document.getElementsByTagName('li');

for (let i = 0; i < geting.length; i++) {
//remove list containing John
	if(geting[i].innerHTML=="John"){
		geting[i].style.display = "none";
	}
//adding a border to list containing Pete
	if (geting[i].innerHTML=="Pete") {
		geting[i].style.border ="1px solid black"
	}

	}

	//getting body element
	let main = document.querySelector("body");
	main.style.fontSize = "70px"