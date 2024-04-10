import time

## Please memorize this :

def decorator(myfunction):
    def wrapper():
        myfunction()
    return wrapper

# decorator : add something to some functions
    
def delay_decorator(f):
    def wrapper():
        time.sleep(2)
        f()
    return wrapper

def timer(f):
    def wrapper():
        s = time.time()
        f()
        e = time.time()
        print("Took ", end='')
        print(e-s)
    return wrapper


@delay_decorator
def sayHello():
    print("hello")
    
@timer
def aaaaaa():
    for i in range(100000000):
        pass

# the above line is equivalent to
# f = delay_decorator(sayHello)
# f()

aaaaaa()