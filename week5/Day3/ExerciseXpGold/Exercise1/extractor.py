#extracting 

match = input("enter mixed text")
def determine(matching):
    mp = []
    for i in matching:
        if i.isdigit():
            mp.append(i)

    print("".join(mp))
determine(match)




        