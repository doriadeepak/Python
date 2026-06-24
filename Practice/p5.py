#finding Average in a loop
sum=0
count=0

for num in [2,4,5,34,56,75,3,6,7] :
    sum+=num
    count+=1
    print(num,sum,count)

print("Sum: ",sum," Count: ",count)
print("Average is: ", sum/count)
