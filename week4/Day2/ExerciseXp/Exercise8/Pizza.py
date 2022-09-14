#Who ordered a pizza
store = ' '
while True:
    store = input("Enter your pizza\n")
    if store != "quit":
        print("I will add topping to user pizza\n")
        newr = []
        newr.append(store)
        continue
    if store == "quit":
        print(newr)
        break
    


