# What is the season?

#int () to convert user in put into number
UserAsk = int( input("Enter a number between 1 and 12 bro\n") )

if UserAsk >= 1 and UserAsk <= 12:
    if UserAsk >= 1 and UserAsk <= 2:
        print(" Winter runs from December (12) to February (2)")
    elif UserAsk >= 3 and UserAsk <= 5:
       print("Spring runs from March (3) to May(5)")
    elif UserAsk >= 6 and UserAsk <= 8:
       print("Summer runs from June(6) to August(8)")
    elif UserAsk >= 9 and UserAsk <= 11:
        print("Autumn runs from September(9) to November (11)")
    else:
        print("Winter runs from December (12) to February (2)")
        
else:
    print("Wrong input")
        
