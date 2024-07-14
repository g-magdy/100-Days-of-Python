'''
unlimited positional argument *args
unlimited keyword arguments **kwargs coming from (not python)
'''
# *args is a tuple of arguments of arbitrary size
def add(*args):
    sum = 0
    for a in args:
        sum += a
    return sum

# print(add(1, 2, 1, 1, 1, 0))

'''
Benefit is that you can look through all of the inputs
and find the ones that you want
and use them to da something
'''
def add2(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


# add2(aba = 21, abb = 32, lol = 123.6)
    # there is one problem in the next two lines
    # that is if you did not specify a value for add or multiply
    # it will give you a KeyError

class Car:
    def __init__(self, **kw):
    # there is a problem here with accessing kw using square brackets, 
    # if a "color" or "model" or "make" does not exist it will throw an error
        self.kwargs = kw
        # self.color = kw["color"] # or you can use self.kwargs["color"]
        # self.model = kw["model"]
        # self.make = kw["make"]
        self.color = kw.get("color")
        self.model = kw.get("model")
        self.make= kw.get("make")
    
    
    def show(self):
        print(self.kwargs)
        
myfriend = Car(color="Blue", model="Chiron")
myfriend.show()