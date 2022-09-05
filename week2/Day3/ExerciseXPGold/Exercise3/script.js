// JS External file

let age = [20,5,12,43,98,55];
let sum = 0;
let z;
for(let i=0; i<age.length; i++){
   sum += age[i];
}
console.log(`The sum is ${sum}`);

for(let t = 0; t<age.length; t++){
	for(let j = 0; j<age.length;j++){
		if(age[j]<age[j+1]){
			z=age[j+1];
			age[j+1]=age[j];
			age[j]=z;
		}
	}
}
console.log(`The maximum number is ${age[0]}`);
