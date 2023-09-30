def add(*args):
    s = 0
    for a in args:
        s += float(a)
    return s

def multiply(*args):
    s = 1
    for a in args:
        s *= float(a)
    return s

# functions are first class objects
# functions can be passed as arguments
# functions can be returned from other functions
def calc(func, *args):
    print(type(args))
    print(*args)
    return func(*args)

# print(calc(multiply, 1, 4, 6))

# functions can be returned
# the activator is the ()

def outer():
    print("outer")
    
    def nested():
        print("nested")
        
    return nested

output = outer()

output()