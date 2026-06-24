def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
    except:
        return "Enter a numeric value"

    if hours>40:
        pay = 40*rate + (hours-40)*(rate*1.5)
    else:
        pay = hours*rate
    return pay 

hrs = input("Enter hours: ")
rate = input("Enter rate: ")

print("Pay: ", computepay(hrs,rate))
