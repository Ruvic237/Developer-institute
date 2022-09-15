# Add your own birthday

birthday = {
    "Ruvic":"2004/02/14",
    "Duvent":"2003/07/7",
    "Yves":"1998/05/21",
    "Pascal":"1996/08/30",
    "Junior":"1994/06/25",
}
print("Welcome dear user\n")
store = input("Enter any name to add\n")
store1 = input("Enter bithday in format “YYYY/MM/DD” \n")
locali = {
    store:store1,
} 
birthday.update(locali)

store2 = input("Enter the name to look\n")
for (name,date) in birthday.items():
    if store2 == name:
        print("{} birthday is in the year {}".format(name,date))
    elif store == name:
        print("{} birthday is in the year {}".format(name,date))
        break