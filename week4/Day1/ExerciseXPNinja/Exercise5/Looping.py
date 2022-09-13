# loop for user to find longest character

from hashlib import new


word = input("Enter the biggest word without a")

if ("a" in word == False):
    while(len(word) > 0):
        new = input("Enter again")
        
        if(len(new) > len(word)):
            print("Congratulaion")
            
        else:
            print("try again")
            
else:
    print("not good")