# run in debug mode
# adding paths to urls
# variables in urls
# using converters with urls#

from flask import Flask

# DEFINE DECORATORS
def bold(myfunc):
    def wrapp():
        return f"<b>{myfunc()}</b>"
    return wrapp

def italic(myfunc):
    def wrapp():
        return f"<em>{myfunc()}</em>"
    return wrapp

def underline(myfunc):
    def wrapp():
        return f"<u>{myfunc()}</u>"
    return wrapp

app = Flask(__name__)

@app.route('/', endpoint='/')
@bold
def home():
    return "Homepage"

# add different route
@app.route('/hello', endpoint='hello')
@italic
def hello():
    return 'hello'

#variables in urls
@app.route("/greet/<name>/<bd>")
def greet(name, bd):
    return f"HI {name}! your birthday is {bd}"

# extracting data - variables from the urls
# specify data type of variable
@app.route("/users/<path:name>/<int:mm>")
def users(name, mm):
    return f"Users {name} >>>> {mm+1}"

if __name__ == "__main__":
    app.run(debug=True)