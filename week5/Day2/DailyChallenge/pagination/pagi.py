#pagination program

from os import remove


class Pagination:
    def __init__(self,items,pagesize):   
        self.items = items
        self.store = []
        self.pageSize = pagesize
        
    def show_page1(self):
        t = 0
        for i in self.items:
            if t<self.pageSize:
                self.store.append(i)
                t+=1
            else:
                break
        print(self.store)
    
    def Next_page(self):
        t = 0
        for i in self.items:
            if t < self.pageSize + self.pageSize:
                self.store.append(i)
                if t < self.pageSize:
                    self.store.remove(i)
                t += 1
            else:
                break
        print(self.store)
        
    def Prev_page(self):
        t = 0
        for i in self.items:
            if t < self.pageSize + self.pageSize:
                self.store.append(i)
                if t >= self.pageSize:
                    self.store.remove(i)
                t += 1
            else:
                break
        print(self.store)
                
    
    def getVisibleItems(self):
         self.show_page1()
        # self.Next_page()
        # self.Prev_page()
        
        
        


show = Pagination(["a","b","c","d"],3)
show.getVisibleItems()

    
    