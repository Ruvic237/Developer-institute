import random

#  Input to stop the game
print("Enter 100 to stop game")

#  Let us generate random numbers
computer = random.choice(range(0, 11))

#  Let us get user input inside a while loop
while True:
    user = int(input("Enter a number between (0:10)  "))
    if 0 <= user < 11:
        if user == computer:
            print("Wow!! You won bro")
            break
        else:
            print("Ohh!! you lose")
    elif user == 100:
        break
    else:
        print("wrong input try again")



