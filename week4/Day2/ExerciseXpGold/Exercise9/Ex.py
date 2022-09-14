# Random Number
import random

while True:
    check = int(input("Enter a number from one to nine\n"))
    ui = random.randint(1,10)
    if check >=1 and check<=9:
            if check == ui:
                store = (print("Winner"))
                reserve = store.count()
                break
            else:
                test = input("do you continue\n")
                if test == "yes":
                    store1 = (print("ok"))
                    reserve1=store1.count()
                    continue
                elif test == "no":
                    break
                
                
print("You won",reserve, "and lost" ,reserve1, "times")
                
                
            
            
        
