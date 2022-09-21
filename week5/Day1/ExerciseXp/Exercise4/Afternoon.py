# afetr noon

class Zoo(dict):
    def __init__(self,zoo_name):
        self.name = zoo_name
        self.animals = {}
    
    def add_animals(self):
        for new_animal in self.animals:
            if new_animal not in self.animals:
                self.animals.append(new_animal)
            else:
                print("it is there")
                
    def get_animals(self):
        for new_animal in self.animals:
            print(new_animal)
            
show = Zoo("Mvogbetsi")
show.add_animals("yo")
show.get_animals()

    
        
        
        