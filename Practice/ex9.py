# fhand=open("mbox.txt")

# count=0
# emails=list()
# for line in fhand:
#     if line.startswith("From"):
#         words=line.strip().split()
#         count+=1

#         #Guardian
#         if len(words)<2:
#             continue

#         emails.append(words[1])
# # emails= list((emails))

# for email in emails:
#     print(email)

fhand=open("mbox.txt")

for line in fhand:
    line=line.rstrip()
    wds=line.split()

    ## Guardian comes before 

    if len(wds)<3 or wds[0]!="From":
    # if wds[0]!="From" or len(wds)<3:
        continue
    print(wds[2])
