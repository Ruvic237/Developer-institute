#generate strings
import string
import random
stru = string.ascii_letters
store = []
for i in range(5):
    store.append(random.choice(stru))

print(''.join(store))



    

    