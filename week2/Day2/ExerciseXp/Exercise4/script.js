// JS external file

let users = ["Lea123"];

let online = users.length;

for (let i =1; i<=users.length; i++) {

if(online == 0){
	console.log("no one is online");
	break;
}
else if (online == 1) {
	console.log(`${i} is online`);
	break;
}
else if (online == 2)
{
	console.log(`${i} are online`);
	break;
}
else(online > 2)
{
	console.log(`${users[i]} are online`);
	break;
}

}