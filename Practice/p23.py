import csv

students=[]

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # students.append({"name":row['name'], "house": row['home']})
        students.append(row)  # same as above T-T
    
def get_name(student):
    return student['name']

for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is from {student['home']}")
