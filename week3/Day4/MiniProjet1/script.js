// JS External file

let getDiv = document.getElementById("Empty");

for(let i = 0; i<1440;i++){
	let newDiv = document.createElement("div");
	let okay = getDiv.appendChild(newDiv);
	okay.classList.add("styling")
}