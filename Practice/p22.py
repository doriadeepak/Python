file=open("names.txt","a")

while True:
    name = input("What's your name?: ")
    if name.lower() in {"exit",""}:
        break
    file.write(f"{name}\n")

file.close()