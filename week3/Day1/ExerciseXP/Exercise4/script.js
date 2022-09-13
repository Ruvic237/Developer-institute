//External JS file

//creation of an array of objects
let arra1 = [
{
	title:"Harrypotter",
	author:"Ruvic",
	image:"absent",
	alreadyRead:true
},
{
	title:"Blackpanther",
	author:"James",
	image:"absent",
	alreadyRead:false
}
]

//for loop for looping in the array of object
for(let i=0;i<arra1.length;i++){
	console.log(`${arra1[i].title} written by ${arra1[i].author}`);
    if(arra1[i].alreadyRead==true){
    	let para = document.getElementsByClassName('listbooks')[0];
    	let para1 = document.createElement("p");
    	para.appendChild(para1);
    	para1.innerHTML = arra1[i].title +" " + "written by"+" "+ arra1[i].author;
    	para1.style.color = "red";

    }

}
