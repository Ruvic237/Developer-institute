// JS external file

// Part 1 of exercise 2
// Declarations and assignment of useful variables series

let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
var ruv = "black mirror, money heist, and the big bang theory";
let myWatchedSeriesLength=myWatchedSeries.length;
console.log(`The total number os series is ${myWatchedSeriesLength}`)
let myWatchedSeriesSentence=myWatchedSeries[1].length;
console.log(`The serie I have watched contains ${myWatchedSeriesSentence} letters`);
console.log(`I watched ${myWatchedSeriesLength} series : ${ruv}`);

// part 2 of exercise 2
// Using push and pop to add and remove items from an array

myWatchedSeries.push("Spider Man");
myWatchedSeries.splice(1,1);
myWatchedSeries.splice(0,2, "Avengers" , "black mirror");
console.log(myWatchedSeries);
let text = "Money heist";
let letter = text.charAt(2);
console.log(letter);
console.log(myWatchedSeries);
//  End of operation

