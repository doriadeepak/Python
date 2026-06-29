from functools import reduce

shout=lambda x: x.upper()

celcius=[0,10,20,30]
fahrenheit=list(map(lambda x: (x*9/5) + 32, celcius))

words = ["apple", "bat", "cat", "dolphin", "elephant"]
long_words=list(filter(lambda x: len(x)>3, words))

nums = [2, 3, 4, 5]
product=reduce(lambda x,y: x*y, nums)

nums = [1, 2, 3, 4, 5, 6]
squared_evens=list(map(lambda x: x**2,filter(lambda y: y%2==0,nums)))

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students=sorted(students,key=lambda y: y[1])

prices = {"apple": 2.50, "banana": 1.00, "cherry": 3.00, "date": 0.50}
expensive_items=dict(filter(lambda x:x[1]>1.50, prices.items()))

names = ["  aLiCe ", "BOB", "  ", "cHaRliE", ""]
clean_names=list(map(lambda x: x.strip().capitalize(),filter(lambda x: x.strip()!="",names)))