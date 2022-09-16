# encryption program

from pydoc import plain
from turtle import position

plain = input("What do you want to encrypt?\n")
step = int(input("How many shift do you want for encryption?\n"))

def hacking(text,shift): # function with two parameters
    encry_numbers = []
    encry_text = []
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
    
    
    for letter in text: #letter iterates through the plain text to encrypt  
         if letter in lowercase: #check if letter is in lowercase 
            position = lowercase.index(letter) 
            encryptFormula = (position+shift)%26 #calculate the new index were encrypted letter is found
            encry_numbers.append(encryptFormula) #adding the indexes of letters who is to encrypt in an array
            encry_letter = lowercase[encryptFormula] #storing of the new letter who is to encrypt
            encry_text.append(encry_letter) # adding the letter stored in an array to display to user the complete encryption
            
         elif letter in uppercase: #check if letter is in uppercase
            position = uppercase.index(letter)
            encryptFormula = (position+shift)%26 #calculate the new index were encrypted letter is found
            encry_numbers.append(encryptFormula) #adding the indexes of letter who is to encrypt in an array
            encry_letter = uppercase[encryptFormula] #storing of the new letter who is to encrypt
            encry_text.append(encry_letter) # adding the letter stored in an array to display to user the complete encryption
            
    print("the Encrypted result is {}".format("".join(encry_text)))
hacking(plain,step)


    
    
            
            


