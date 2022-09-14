
text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
text1 = text.split()
for x in text1: 
    if text1.count(x)>0:
       print(x,"is", text1.count(x))