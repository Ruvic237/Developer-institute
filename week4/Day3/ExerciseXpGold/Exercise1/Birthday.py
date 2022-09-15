# Birthday lookup

birthday = {
    "Ruvic":"2004/02/14",
    "Duvent":"2003/07/7",
    "Yves":"1998/05/21",
    "Pascal":"1996/08/30",
    "Junior":"1994/06/25",
}
print("Welcome dear user you can look birthday in list")

store = input("Enter the name to look\n")

for (name,date) in birthday.items():
    if store == name:
        print("{} birthday is in the year {}".format(name,date))
        