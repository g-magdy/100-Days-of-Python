print("welcome to the rollercoaster")
h = int(input("What is your height ? "))
if h > 180:
    print("you are welcomed to ride 😉")
    age = int(input("What is your age ? "))
    if age < 12:
        print("pay 5$")
    elif age <= 18:
        print("pay 7$")
    else:
        print("pay 12$")
else:
    print("Get yout you little child")