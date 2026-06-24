#counting lines from a file

count=0
fhand=open("mbox.txt")

for line in fhand:
    count+=1
print("Line Count: ", count)

#reading the whole file at once

fhand=open("mbox.txt")
strng= fhand.read()
print(len(strng))
print(strng[:25])

#searching thru a file

fhand=open("mbox.txt")
for line in fhand:
    if line.startswith("#"):
        # print(line)
        print(line.rstrip())
        