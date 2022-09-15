# advanced birthday

birthday = {
    "Ruvic":"2004/02/14",
    "Duvent":"2003/07/7",
    "Yves":"1998/05/21",
    "Pascal":"1996/08/30",
    "Junior":"1994/06/25",
}
print("people in list are \n",birthday.keys())
print("Welcome dear user\n")
store1 = input("Enter the name to look\n")

for (name,date) in birthday.items():
    if store1 == name:
        print("{} birthday is in the year {}".format(name,date))
    else:
        print("Sorry,we don’t have the birthday information for",store1)
        break
        
        

