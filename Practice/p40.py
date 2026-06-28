# def smart_multiplier(*nums, **bonus):
#     result=1
#     for num in nums:
#         result*=num
#     if bonus:
#         result*=2
#     return result

# print(smart_multiplier(2,3,4, bonus=True))

def make_counter(start_value):
    def increment():
        nonlocal start_value
        start_value+=1
        print(start_value)
    return increment
    
counter=make_counter(10)
counter()
counter()
counter()