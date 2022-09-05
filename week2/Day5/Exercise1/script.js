// JS external file

//start of playgame function
function playTheGame(){

    let txt = "Do you want to play?";

    //if user clicks ok
    if(confirm(txt) == true){

        //Prompting user to get his input
        let store = Number(prompt("Enter a number between 0 and 10 user"));

        //determine if number is in range
        // if(store>=0 && store<=10){
        //     let computerNumber = Math.floor(Math.random()*10);
        //     compareNumbers(store,computerNumber);
            
        // }

        //Determine if number is a number or not
        if(isNaN(store)){
            alert("Sorry Not a number, Goodbye");
        }
        else if(store>=0 && store<=10){
            let computerNumber = Math.floor(Math.random()*10);
            compareNumbers(store,computerNumber);
            
        }

        //Determine if number is out of range
       else{
            alert("Sorry it’s not a good number, Goodbye");
        }
        
    }
    //end of okay clicking

   //if user clicks annuler
    else
    {
        alert("No problem, Goodbye");
    }
    //end of annuler 
     

}

 
 
//  start of function compare
   function compareNumbers(store , computerNumber){
    for(let i = 0; i <= 1; i++){
        if(store == computerNumber){
             alert("WINNER");
             return;
        }
        else if(i == 1){
            alert("Too many tries the answer is"+ " " + computerNumber);
            return;
        }
         else if(store > computerNumber){             
            store = prompt("Too big guess again");
        }
         else(store < computerNumber)
        {
            store = prompt("Too small guess again");
        }
    }
 }

