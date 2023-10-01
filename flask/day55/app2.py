from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Home"


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.is_logged_in = False
        
    def login(self):
        self.is_logged_in = True
        
        
def require_auth(myfunc):
    def wrp(*args, **kwargs):
        if args[0].is_logged_in:
            myfunc(args[0])
        else:
            print("unauthenticated")
    return wrp

# not intuitive to be outside. but let it be, to test something.
@require_auth
def create_blog_post(user):
    print(f"Hi, this is {user.name}'s blog post")

new_user = User("George")
new_user.login()
create_blog_post(new_user)

def log(myfunc):
    def wrp(*args):
        print(f"Called {myfunc.__name__}{args}")
        rv = myfunc(*args)
        print(f"Returned {rv}")
    return wrp
        