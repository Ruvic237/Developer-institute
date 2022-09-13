// JS External file

// Part 1
// using setTimeout, to call a function after 2 seconds.To alert "Hello World"

//Function creation
function Text(){
	alert("Hello World");
}
//End of function

//use of setTimeout to Assign the time to display the text to be alerted in the function
setTimeout(Text,2000);
//end

//Part 2
//using setTimeout, to call a function that will add a new paragraph to the div after 2s

//Function creation 
function TextParagraph(){
	let parent1 = document.getElementById("container");
	let childPara = document.createElement("p");
	let addedChildPara = parent1.appendChild(childPara);
	addedChildPara.innerHTML = "Hello World!";
}
//End of function

//use of setTimeout to Assign the time to display the text of paragraph in webpage function
setTimeout(TextParagraph,2000);

//part3

//A variable to store the repetition of adding paragraphs in the div done in a function
let store = setInterval(Creating,2000);

//Creating the function Creating
function Creating(){
	let parent1 = document.getElementById("container");
	let childPara = document.createElement("p");
	let addedChildPara = parent1.appendChild(childPara);
	addedChildPara.innerHTML = "Hello World!";

}

//An onclick event function -->clearing for button which when clicked stops creating paragraphs

function clearing(){
	clearInterval(store);
}//End





