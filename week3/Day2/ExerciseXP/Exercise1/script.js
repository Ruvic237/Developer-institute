 //Collect the h1 tag
 let newH = document.getElementsByTagName("h1")[0];
 console.log(newH);

 //collect the parent last child
 let newHi = document.getElementsByTagName("article")[0].lastElementChild;
 newHi.remove();
 console.log(newHi);

//collect the h2 element to change color on click using event listener
 let newHir = document.getElementsByTagName("h2")[0];

//addind the event listener with the call back of test as a function
 newHir.addEventListener("click",test);

//function call for the h2 event listener
 function test(){
    newHir.style.color = "red";
 }

 //collecting the h3 element
 let newHire = document.querySelector("h3");

//addind the event listener with the call back of test as a function
 newHire.addEventListener("click",erase);

//function call for the h2 event listener
 function erase(){
    newHire.style.display = "none";
 }

//Calling parent element to add child 
let fath = document.querySelector("article");
let newb = document.createElement("button");
fath.appendChild(newb);
//creation done

//calling button to add innertext
let share =document.querySelector("button");
share.innerHTML = "Click Here";

//Selecting all paragraphs
let newP = document.querySelectorAll("p");

//use the button variable to perform operation
share.addEventListener("click",perform);

function perform(){
    //use a for loop to iterate through each index of paragraph
    for(let i=0;i<3;i++){

        newP[i].style.fontWeight = "bold";
 }
}




