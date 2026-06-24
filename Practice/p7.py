#search using a bololean variable

Found = False
for num in [9,41,12,3,74,15]:
    if num==3:
        Found = True
    print(Found, num)
    if Found == True : break
print("Finally: ", Found)