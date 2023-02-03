name = input("Hello 😀\nWhat is your name? ")
print("Welcome to Python " + name + "!")
word = input("See the length of your name ? (y/n) ")
if word == "y":
    print("The length of your name is " + str(len(name)))
else:
    print("Goodbye 👋")