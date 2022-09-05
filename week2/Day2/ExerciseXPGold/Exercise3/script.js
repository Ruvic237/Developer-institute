// JS external file

// Prompt the user for a string. It must be a verb.
// If the length of the string is at least 3 and the string doesn’t end with “ing”, add ‘ing’ to the end of the string.
// If the length of the string is at least 3 and the string ends with “ing” add “ly” to it’s end.
// If the length of the string is less than 3, leave it unchanged.

let verb = prompt("Dear user enter only a verb");
let cheh = verb.endsWith("ing");

if(verb.length >= 3 && cheh==false){
    alert(verb+"ing");
}
else if(verb.length >= 3 && cheh==true){
    alert(verb+"ly");
}
else(verb.length<3)
{
    alert(verb);
}