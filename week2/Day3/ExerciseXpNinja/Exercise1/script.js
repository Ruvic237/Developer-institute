// JS external file

let person1 = {
    FullName:"Ruvic",
    Mass:50,
    Height:1.8,
    Mbi: function(){
        return this.Mass/(this.Height^2);
    }
    
}

let person2 = {
    FullName:"Yves",
    Mass:Number(90),
    Height:1.7,
    Mbi: function(){
        return this.Mass/(this.Height^2);
    }
    }

 if (person1.Mbi()>person2.Mbi()) {
    alert(`${person1.FullName} has biggest BMI`);
 }
 else
 {
   alert(`${person2.FullName} has biggest BMI`); 
 }
