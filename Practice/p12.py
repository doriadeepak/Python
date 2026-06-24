colors = """red,
orange,
green,
purple,
yellow"""

print(colors.split())
print(colors.split(','))
print(colors.split(',\n'))

print("\n")

new_list = colors.split()
text = " ".join(new_list)
print(new_list)
print(text)