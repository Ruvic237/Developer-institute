// JS external file

let building = {
	numberOfFloors:4,
	numberOfAptByFloors:{
		firstFloor:3,
		secondFloor:4,
		thirdFloor:9,
		fourthFloor:2,
	},
	nameOfTenants :["Sarah","Dan","David"],
	numberOfRoomsAndRent:{
		sarah:[3,990],
		dah:[4,1000],
		david:[1,500],
	},
}

console.log(building.numberOfFloors);
console.log(`${building.numberOfAptByFloors.firstFloor} and ${building.numberOfAptByFloors.thirdFloor}`);
console.log(`${building.nameOfTenants[1]} has ${building.numberOfRoomsAndRent.dah[0]} rooms`);

let sum1 = building.numberOfRoomsAndRent.sarah[1]+building.numberOfRoomsAndRent.david[1];
let sum2 = building.numberOfRoomsAndRent.dah[1];
if (sum1>sum2) {
	sum2=1200;
	console.log(sum2);
}


