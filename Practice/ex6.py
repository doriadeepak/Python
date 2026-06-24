total=0
count=0
while True:
    user_input=input("Enter a number: ")
    if user_input.lower() == "done":
        break
    try:
        total+=int(user_input)
        count+=1
    except:
        print("Invalid input")
        continue
print("Total: ",total,"\n", "Count: ",count,"\n","Average: ",total/count)