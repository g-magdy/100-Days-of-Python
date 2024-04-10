def require_authentication(f):
    def wrapper(*args, **kwargs):
        u : User = args[0]
        if (u.is_logged_in == True):
            f(*args, **kwargs) # ! * args and *kwargs solve the problem of passing "self" 
        else:
            print("You need to login first")
    return wrapper    


class User:
    
    def __init__(self) -> None:
        self.username = ""
        self.is_logged_in = False
    
    @require_authentication
    def post(self):
        print(f' {self.username} posted a new post')    
        


# mark = User()
# mark.username = "mark"
# mark.is_logged_in = True
# mark.post()



def logging_decorator(f):
    def wrapper(*args, **kwargs):
        print(f'{f.__name__} was called')
        print('arguments are: ', end='')
        for arg in args:
            print(arg)
        v = f(*args, **kwargs) #! important *args, **kwargs
        print(f"returned {v}")
    return wrapper


@logging_decorator
def myfunc(*args, **kwargs):
    sum = 0
    for arg in args:
        sum += int(arg)
    return sum

myfunc(1, 2, 3, 4)