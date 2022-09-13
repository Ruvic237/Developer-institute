//JS External file

//getting the the div element to change attribute using setAttribute
let select = document.getElementById("navBar");
select.setAttribute("id","socialNetworkNavigation");

//Creation of an li element
let main = document.getElementById("socialNetworkNavigation");
let creat1 = document.createElement("li");
creat1.innerHTML = "Logout";
main.appendChild(creat1);