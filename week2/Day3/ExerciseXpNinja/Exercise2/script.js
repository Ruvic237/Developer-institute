// JS external file



function findAvg(gradesList){
	let sum =0;

	for(let i =0; i<gradesList.length;i++){
		sum = sum + gradesList[i];
	} 
	return sum/(gradesList.length);
}
 
 let gradesList=[5,8,9,7];
 let show = findAvg(gradesList);
 console.log(show);
