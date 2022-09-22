#Random module
import random
coun = 0
while coun < 2:
        choic = int(input(f"Enter a number between 1 and 100 trial {coun}"))
        def Random_Number(select):
                computer = random.choice(range(1,101))
                if select >=1 and select <=100:  
                    if select == computer:
                        print("Woupii you won vs computer")
                        coun < 2 == False
                    else:
                        print("Ohh no computer won")
                else:
                    print("retry again")           
        Random_Number(choic)
        coun+=1
print(f"You attempted {coun} times")