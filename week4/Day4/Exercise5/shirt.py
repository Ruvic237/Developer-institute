#personalized shirts
siz = input("enter the size of shirt\n")
def make_shirt(size,message):
    if size == "small":
        print(f"the size is {size} and the text is I will soon love python")
    else:
        print("The size of the shirt is {} and the text is {}".format(size,message))
make_shirt(siz,message="I love python")



    