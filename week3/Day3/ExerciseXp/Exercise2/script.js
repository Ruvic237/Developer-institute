//JS External file

//Creation of the function for the onclick event of button
function myMove(){
	let getId = document.getElementById("animate");
	let position = 0; //initialisation of a variable to increment later and change the px
	let counter = setInterval(perform,10) // setting amount of time for changing in perfom()

	//Creation of the function to change the position of box from left
	function perform(){

		//setting limit of pixel at 350px using if condition
		if(position==350){
			clearInterval(counter);
		}

		//increasing left style px fo it to shift at the right as position increase
		else{
			position++
			getId.style.left = position + "px"; 
		}
	}
	//end of the function--->perform()

}
//end of the function--->myMove()