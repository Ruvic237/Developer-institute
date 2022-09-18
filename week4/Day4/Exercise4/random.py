#random program
import random

userGuest = int(input("Enter a number to guess\n"))
computerGuest=random.randint(1,101)
def compare(user,computer):
    if user == computer:
        print("You won cool")
    else:
        print("You lost")
    print("You choose {} and computer choose {}".format(user,computer))
compare(userGuest,computerGuest)









