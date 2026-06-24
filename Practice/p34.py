s1={1,2,3}
s2={2,3,4}
s3={3,4,5}

s4=s1.intersection(s2,s3)
s5=s3.difference(s1,s2)
s6=s1.symmetric_difference(s3)

print(s4)
print(s5)
print(s6)