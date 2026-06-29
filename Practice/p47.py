#Q1
scores = [45, 80, 92, 30]
result = ["Pass" if score>=50 else "Fail" for score in scores]

#Q2
pairs = [("a", 1), ("b", 2)]
flat = [item for pair in pairs for item in pair]
