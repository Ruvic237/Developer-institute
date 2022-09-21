
class Dog():
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.add = []
        
    
    def bark(self):
        return f"{self.name} is backing"
    def run_speed(self):
        solve = (self.weight/self.age*10)
    
    def fight(self,dog):
        self.other_dog = dog
        self.add.append(solve)
        for i in self.add:
            if i == max(self.add):
                print(f"the winner is {self.name}")

Show = Dog("Jake",20,50)
John =Dog("ruv",5,89)
Peter = Dog("peter",14,20)
Show.fight("Jako")
John.fight("Feri")
Peter.fight("thiro")


            
        
        
        
    