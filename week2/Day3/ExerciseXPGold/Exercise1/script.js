// JS external file

let numbers = [123,8409,100053,333333333,7];

for(let i=0;i<numbers.length;i++){
	if(numbers[i]%3==0){
		console.log(numbers[i] +" "+ "is True");
		continue;	
	}
	else(numbers[i]%3!=0)
	{
		console.log(numbers[i] +" "+ "is False");
	}
}