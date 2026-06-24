import csv 
import json
import io
from urllib.request import urlopen

csv_data=[]

with urlopen("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv") as response:
    text_file = io.TextIOWrapper(response, encoding="utf-8")
    data=csv.DictReader(text_file)
    for row in data:
        csv_data.append(row)
print(csv_data)