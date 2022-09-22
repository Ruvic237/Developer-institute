#Built in functions

from ast import arg


# absolute = abs(-20.25)
# print(absolute)

# interger = int(20.89)
# print(interger)

# store = input("what is your name?")
# print(store)

class Person():
    """ A code to find an absolute value"""
    def __init__(self,argument):
        self.argument = argument
    def show(self):
        print(abs(self.argument))
        print(Person.__doc__)

briefing = Person(50.13)
briefing.show()



        
        
        