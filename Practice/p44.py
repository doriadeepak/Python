#syntax==>  new_list=[expression for item in iterable if condition]

##EX1
squares=[x**2 for x in range(10)]
print(squares)

#EX2
squares_even=[x**2 for x in range(10) if x%2==0]
print(squares_even)

#EX3
names=["alice","bob","charlie"]
capitalized_names=[name.capitalize() for name in names]
print(capitalized_names)