// JS external file
// Program to generate a calculator

let num1 = prompt("Enter the first number");
console.log(typeof Number(num1));
let num2 = prompt("Enter the second number");
console.log(typeof Number(num2));
let sum = Number(num1) + Number(num2);
let sub = Number(num1) - Number(num2);
let div = Number(num1) / Number(num2);
let mul = Number(num1) * Number(num2);
alert(`The sum is ${sum}`);
alert(`The difference is ${sub}`);
alert(`The division is ${div}`);
alert(`The multiplication is ${mul}`);
