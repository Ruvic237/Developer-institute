// JS external file
// Zip code program


// While working in a Post Office you must have the clients’ zip code in order to send them their letters.
// Ask the client for their zip code and console.log “success” or “error” based on the following rules.
// Zip codes consists of 5 numbers
// Must only contain numbers
// Must not contain any whitespace (spaces)
// Must not be greater than 5 digits in length

let ask = prompt("Enter your zip code dear user");

if(ask.length===5 && isNaN(ask)==false){
	console.log("Success");
}
else{
	console.log("error");
}






