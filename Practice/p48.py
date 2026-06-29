#List comprehensions(Eats Memory)
# squares_list = [x for x in range(10000000000)]
# print(squares_list)

#Generators(Saves Memory)
squares_gen = (x for x in range(100000000))
for i in squares_gen:
    print(i)


# def generate_even_numbers(limit):
#         for x in range(limit):
#             if x % 2 == 0:
#                 yield x  # Pauses here until the next loop!

# # Using it:
# for num in generate_even_numbers(10):
#     print(num)
    