#Asking user for input until he gives the correct input
while True:
    try:
        x= int(input("What is x?: "))
        # "break" here will do the same function as the else loop on line 8 is doing
        ## will function but "can't say if it is better in contect of design"
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")