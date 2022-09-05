// JS external file


//A variable to hold anything a user will insert in the input screen
let hold = document.getElementById("store");



//A function I use to change the default value of hold which is null with onclick function number(num)
let number = function(num){
    hold.value = hold.value + num;
}


//A function I use to change the default value of hold which is null with onclick function operator(sign)
let operator = function(sign){
    hold.value += sign; //concatenation
}


//An eval function is used to solve anything displayed on the screen stored in hold.value
let equal = function(){
    hold.value = eval(hold.value);
}


//An erase function which when called asigns an empty string to hold.value hence screen shows nothing
let erase = function() {
    hold.value = " ";
}

//A reset function which when called by clicking reset assigns a value of 0 hence screen shows 0
let reset = function(){
    hold.value = 0;
}


