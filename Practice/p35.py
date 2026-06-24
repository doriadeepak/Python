# l1=[1,2,3,4,1,2,3,4]

# l2=list(set(l1))

# print(l2)


employees=['Corey','Jim','Steven','April','Judy','Jenn','John','Jane']

gym_members=['April','John','Corey']

developers=['Judy','Corey','Steven','Jane','April']

result1=set(gym_members).intersection(developers)
result2=set(employees).difference(gym_members,developers)
print(result1)
print(result2)

if 'Corey' in developers:
    print("Found!")
#O(n) for list
#O(1) for a set
# to do this stuff above
