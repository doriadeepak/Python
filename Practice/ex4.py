hrs = input("Enter Hours: ")
rate = input("Enter rate: ")

try:
    hrs = float(hrs)
    rate = float(rate)
except:
    print("Error, please enter numeric input") 
    quit()

if hrs>40:
    print("Overtime")
    pay = 40*rate + (hrs-40)*(rate*1.5)
else:
    print("Regular")
    pay = hrs*rate

print("Pay: ",pay)
