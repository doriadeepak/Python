# top 10 most common words

fname=input("Enter file name: ")
fhand=open(fname)

counts=dict()
tmp=list()

for line in fhand:
    wds=line.rstrip().split()
    for word in wds:
        counts[word]=counts.get(word,0)+1

# for k,v in counts.items():
#     tmp.append((v,k))
# tmp=sorted(tmp,reverse=True)


tmp=sorted([(v,k) for k,v in counts.items()],reverse=True)[:10]
   
for v,k in tmp[:10]:
    print(k,v)