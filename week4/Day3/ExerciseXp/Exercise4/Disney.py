#Disney Characters
import numbers

names = ["Mikey","Minnie","Donald","Ariel","Pluto"]
numbersr = [i for i in range(0,len(names))] #array of numbers

show = dict(zip(names,numbersr)) # join corresponding index in a dict
print(show)

show1 = dict(zip(numbersr,names)) # join corresponding index in a dict
print(show1)

namesort = sorted(names) #sorting out array first
show3=dict(zip(namesort,numbersr)) # join corresponding index in a dict
print(show3)

news =[]
for letter in names:
    if ('i' in letter) or (letter[0]=='m' or letter[0] == 'p'):
        news.append(letter)
        numbersr = [i for i in range(0,len(news))] #array of numbers
        show4 = dict(zip(news,numbersr)) # join corresponding index in a dict
        print(show4)

        
        
        
        


