numbers = [1, 2, 3]
### new list = [newItem for item in list] ###
newList = [n*13 for n in numbers]
print(newList)

# Python sequences : list, tuple, range, string

name = "George"
chars = [c.upper() for c in name]
print(chars)

d = [2*i for i in range(1, 5)]
print(d)

# CONDITIONAL LIST COMPREHENSION

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

filtered = [name.upper() for name in names if len(name) > 5]
print(filtered)