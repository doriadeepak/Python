# #task-1
hours = input("Enter hours worked: ")
rate = input("Enter hourly rate: ")

try:
    total_pay = float(hours) * float(rate)
except ValueError:
    print("Error, please enter numeric input")
else:
    print(f"Total pay: ${total_pay}")

#task-2
while True:
    user_input=input("Enter a number (or type 'done' to quit): ")
    if user_input == "done":
        break
    try:
        user_input=float(user_input)
    except ValueError:
        print("Invalid input, try again")
    else:
        print(f"Good job, you entered: {user_input}")
        