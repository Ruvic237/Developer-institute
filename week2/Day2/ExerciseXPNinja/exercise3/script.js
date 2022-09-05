// JS external file

let word = prompt("Enter a word dear user")

let regex = /[aeiou]/gi;
let result = word.replace(regex,"t");
console.log(result);

