#cats
from unicodedata import name


class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
      
cat1 = Cat("Minou",30)
cat2 = Cat("Miaou",40)
cat3 = Cat("Jako",80)

def check():
    if cat1.age > cat2.age and cat1.age > cat3.age:
        print("the cat name is {} and is {} age".format(cat1.name,cat1.age))
    elif cat2.age > cat1.age and cat2.age > cat3.age:
        print("the cat name is {} and is {} age".format(cat2.name,cat2.age))
    elif cat3.age > cat1.age and cat3.age > cat2.age:
        print("the cat name is {} and is {} age".format(cat3.name,cat3.age))
    else:
        print("Equal ages")   

check()
       
        
