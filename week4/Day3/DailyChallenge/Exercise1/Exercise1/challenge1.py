
ask = input("Enter a word \n")
empty = {}
for (index,letter) in enumerate (ask):
    # if letter not in empty:
        empty[letter] = []
        empty[letter].append(index)
print(empty)
    

