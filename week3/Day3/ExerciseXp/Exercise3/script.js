//JS External file

//storing the element to be draggable
let dragElement = document.getElementById("box");
let drop = document.getElementById("target");

//Event listener of ondrag start for the element
dragElement.addEventListener("ondragstart",dragFunction);

//calling the function of dragFunction
function dragFunction(event){
	let y = event.dataTransfer.setData("text/plain",event.target.dragElement);
	event.dataTransfer.effectAllowed = "move";
}

function accept(event){
	event.preventDefault();
	let u = event.getData("text/plain");
	u.appendChild(y);
    
}