
string1 = input("Enter a word with duplicate consecutive letters")
remove = ''.join(dict.fromkeys(string1)) # convert string characters to dictionary keys eliminate all duplicates

print(remove)
    