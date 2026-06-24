#Finding smallest value

# numbers = [9,41,12,3,74,15]
# smallest=numbers[0]
# for num in numbers:
#     if num<smallest:
#         smallest=num
#     print(num, smallest)
# print("Smallest number is: ",smallest)

#OR

smallest = None
for num in [9,41,12,3,74,15]:
    if smallest is None:
        smallest=num
    elif num<smallest:
        smallest=num
    print(num, smallest)
print("Smallest number is: ",smallest)

