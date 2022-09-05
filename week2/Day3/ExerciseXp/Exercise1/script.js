// JS external file

let people = ["Greg","Mary","Devon","James"];

// part 1

people.shift();
console.log(people);
people.splice(2,1,"Jason");
console.log(people);
people.push("Ruvic");
console.log(people);
console.log(people.indexOf("Mary"));
console.log(people.slice(1,3));
console.log(people.indexOf("Foo"));//Because it is not in array

let last = people[3];
console.log(last);// length of array gives us number items 

//part 2

for(let i=0;i<people.length;i++){
	if (people[i]=="Jason") {
		break;
	}
	console.log("Jason");
}
