fname=input("Enter File-name: ")
fhand=open(fname)

for line in fhand:
    line=line.upper().strip()
    print(line)
