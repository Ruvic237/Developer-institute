# A cool program
import random

Submit = input("Enter a string of atleast 10 characters\n")
length = len(Submit)

if length < 10:
    print("string not long enough")

elif length > 10:
    print("string too long")
    
elif length == 10:
    cons = ""
    for i in Submit:
        cons = cons + i
        print(cons)
        
# shuffel is used only on list so convert string to list using --> list . strip()         
maini = list(Submit.strip())       
random.shuffle(maini)

#"" .join(what to remove space)
mainistring = "" .join(maini)

print(mainistring)
    
        