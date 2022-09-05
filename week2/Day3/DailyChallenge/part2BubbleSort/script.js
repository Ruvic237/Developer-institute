// JS external file

const numbers = [5,0,9,1,7,4,2,6,3,8];
console.log(numbers.toString());

let temporary = 0;
for(let i = 0; i<=numbers.length;i++){
    for(let j = 0; j<=numbers.length;j++){
        if(numbers[j]<numbers[j+1]){
            temporary=numbers[j+1];
            numbers[j+1]=numbers[j];
            numbers[j]=temporary
        }
    }
}
console.log(numbers.toString());
