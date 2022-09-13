// JS External file

//Since body is parent we access first child of body to display table
let table = document.body.firstElementChild;

//table is parent so we need to call access all table row so in for we avoid decidind index our selves
let row = document.querySelectorAll("tr");
console.log(row);

for(let i = 1; i<=row.length;i++){
	 let colon = document.querySelector(`tr:nth-of-type(${i}) td:nth-of-type(${i})`);
	 colon.style.backgroundColor = "red";
	 console.log(colon);
}



