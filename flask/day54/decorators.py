import time
# the decorator function is just a normal function
# it takes another function as input; let it be f1
# it triggers f1
# then returns a wrapper function in which f1 is called
# the wrapper function is a nested function defined inside the decorator function#

        # the wrapper gives the passed function additional functionality
        # you can specify a behaviour before or after calling the function
        # this behaviour is defined in the wrpper function

def decorate(myfun):
    def wrapper():
        time.sleep(2)
        myfun()
        print(f"delayed by 2 sec")
    return wrapper

def say_hello():
    print("hello")


def decorate2(myfun):
    def wrap():
        time.sleep(3)
        myfun()
        print(f"delayed by 3 sec")
    return wrap

@decorate2 # syntactic sugar
def say_bye():
    print("goodbye")


decorated = decorate(say_hello)
decorated()

say_bye()
