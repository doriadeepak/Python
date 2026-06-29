#Q1
cube_gen=(x**3 for x in range(1,6))

#Q2
def countdown(n):
    for x in range(n):
        yield n-x

n=int(input("Enter n: "))
for count in countdown(n):
    print(count)