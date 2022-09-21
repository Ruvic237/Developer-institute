# Geometry program

import math

class Radius():
    def __init__(self,radius=1.0):
     self.radius = radius
    def Calculate_Area(self):
            self.area = math.pi*(self.radius)**2
            return self.area
    
        
    def Calculate_Perimeter(self):
            self.perimeter= 2*math.pi*(self.radius)
            return self.perimeter
Show = Radius()
t = round(Show.Calculate_Area(),3)
v = round(Show.Calculate_Perimeter(),2)
print("The area of circle is {} and perimeter is {}".format(t,v))


        
        