#BAD file names

fname= input("Enter file name: ")
try:
    fhand= open(fname)
except:
    print("File cannot be opened.")
    quit()
count=0
for line in fhand:
    if line.startswith("#"):
        count+=1
print("There are",count,"# lines in ",fname)
