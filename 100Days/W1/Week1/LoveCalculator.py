name1 = input("name1 = ")
name2 = input("name2 = ")
word = (name1 + name2).lower()

n1 = word.count('t') + word.count('r') + word.count('u') + word.count('e')
n2 = word.count('l') + word.count('o') + word.count('v') + word.count('e')

score = int (str(n1) + str(n2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")