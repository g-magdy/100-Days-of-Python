# Many arguments
def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


mylist = [1, 4, 5, 6, 2, 7]

# print(add(mylist[0], mylist[1]))

# Many keyword arguments
def calc(num, **kwargs):
    try:
        num += kwargs.get("add")
        num *= kwargs.get("multiply")
        return num
    except KeyError:
        print("operation does not exist")
        return None
    

print(calc(10, add=12, multiply=2))
