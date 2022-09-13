// JS external file

// Prompt player 1 for a word. The word must have a minimum of 8 letters. Present the word in the console with stars (********).
// At this point continuously prompt player 2 for a letter.
// If the letter is in the word chosen by player 1, display the word in stars again but with the correct letter (*****t**).
// If the letter appears in the word multiple times, make sure it is seen in all the correct places when showing the stars with the correct guesses (***t**t*).
// If player 2 guesses incorrectly 10 times display a message in the console saying YOU LOSE.
// Show a list of all the guesses after each turn. In your code prevent player 2 from guessing the same letter twice.
// If player 1 wins, display a message that says CONGRATS YOU WIN.

let player1 = prompt("Enter A word guy");
let player2 = prompt("Enter A leeter to gues man");
let player = player1.split("");
for(let i=0;i<player.length;i++){
   if(player.length>=8){
    console.log("*".repeat(player.length));
   }
   if(player2==player[i]){
    console.log(player[i])
    break;
   }
}




