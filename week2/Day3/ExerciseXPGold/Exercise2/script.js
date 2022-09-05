// JS External file

let guestList = {
	randy: "Germany",
	karla: "France",
	wendy: "Japan",
	norman:"England",
	sam: "Argentina"
}

let name = prompt("Enter your name dear user");
  
  if(!(name in guestList)){
  	alert("Hi I am a guest");

  }
  else
  {
  	alert(`Hi! I'm ${name},and I am from ${guestList[name]}`);
  }