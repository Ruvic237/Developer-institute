# Custom List Class

class MyList():
    def __init__(self,letter):
        self.letter = letter
    
    def Reverse(self):
        return self.letter[::-1]
    
    def Sorting(self):
        return sorted(self.letter)
    
Show = MyList(["z","r","c","d"])
y = Show.Reverse()
x = Show.Sorting()
print("Sorted list is {}".format(x))
print("Reversed list is {}".format(y))



        
        
    