import random
# create new dictionary using existing dictionaries or existing lists
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']


# new_dict = {key:value for item in list}
scores_dict = {name:random.randint(1, 100) for name in names}
print(scores_dict)

# new_dict = {key:value for (key, value) in oldDict.items()}
passed_dict = {key:value for (key, value) in scores_dict.items() if value > 70}
print(passed_dict)