# Dog class

class Dog():
    def __init__(self,name,height):
        self.name = name
        self.height = height
    
    def bark(self):
        print("{} goes woof!".format(self.name))
        
    def jump(self):
        self.height = self.height * 2
        print("{} jumps {}cm".format(self.name,self.height))

davids_dogs = Dog("Rex",50)
davids_dogs.bark()
davids_dogs.jump()
sarahs_dog = Dog("Teacup",20)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dogs.height > sarahs_dog.height:
    print("{} is the biggest dog".format(davids_dogs.name))
elif sarahs_dog.height > davids_dogs.height:
    print("{} is the biggest dog".format(sarahs_dog.name))
  

        