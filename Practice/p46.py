nums = [1, 2, 3, 4]
labels=["Even" if x%2==0 else "Odd" for x in nums]

matrix = [[1, 2], [3, 4], [5, 6]]
flat=[num for row in matrix for num in row]
print(flat)
