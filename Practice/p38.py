try:
    year= int(input("Year: "))
except ValueError:
    print("Invalid input")
else:
    #Leap year-- if divisible by 4 or 400 else nope if div by 100

    if (year%4==0 and year%100!=0) or year%400==0:
            print("A leap year!!")
    else:
        print("Not a leap year!!")
