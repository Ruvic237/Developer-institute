
from audioop import reverse
from itertools import count


listo = "Volkswagen Toyota Ford Motor Honda Chevrolet"
listo1 =list(sorted(listo.split()))
show = ('').join(listo1)

listoshow = listo1.copy()
listoshow.reverse()

vamo = len(listo1)
print(f"there are {vamo} manaufacturers in list")
print(listoshow)

for check in listo1:
    if "o" in check:
        y = print("yes")
        count("yes")
        
    elif "i" not in check:
        print(count())





