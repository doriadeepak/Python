# cmd1="Lol"
# cmd2="123"
# try:
#     print("No error1")
#     cmd1in=int(cmd1)
#     print("No error2")
# except:
#     cmd1in = -1
# cmd2in=int(cmd2)
# print(cmd1in)
# print(cmd2in)


inp= input("Enter a number: ")
ival = 1
try:
    num = int(inp)
except:
    ival = -1
    num = -1

print(num)

if ival>0:
    print("Good job!!")
else:
    print("NaN")