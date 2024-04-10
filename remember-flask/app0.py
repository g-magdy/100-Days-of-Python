from flask import Flask
app = Flask(__name__)

def make_bold(f):
    def wrapper():
        return "<b>"+f()+"</b>"
    return wrapper


def make_underline(f):
    def wrapper():
        return "<u>"+f()+"</u>"
    return wrapper

def make_italic(f):
    def wrapper():
        return "<em>"+f()+"</em>"
    return wrapper
    

@app.route("/")
@make_bold
@make_italic
@make_underline
def hello():
    return "Welcome back, friend"

if __name__ == "__main__":
    app.run(debug=True)
    
