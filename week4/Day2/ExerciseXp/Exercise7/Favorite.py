#Favorite fruit

get = input("Enter your favorite fruits and seperate with single space\n")
show = get.split() #convert string to list of words

while True:
    show1 = input("enter a fruit\n")
    if show1 in show:
        print("You have choosen one of your fruits")
        break
    else:
        print("You have choosen a new fruit enjoy")
        break

