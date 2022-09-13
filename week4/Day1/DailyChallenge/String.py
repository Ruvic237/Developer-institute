# A cool program

Submit = input("Enter a string of atleast 10 characters\n")
length = len(Submit)

if length < 10:
    print("string not long enough")

elif length > 10:
    print("string too long")
    
elif length == 10:
    print(Submit[0])
    print(Submit[0:2])
    print(Submit[0:3])
    print(Submit[0:4])
    print(Submit[0:5])
    print(Submit[0:6])
    print(Submit[0:7])
    print(Submit[0:8])
    print(Submit[0:9])
    print(Submit[0:10])
    
        