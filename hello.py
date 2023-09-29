from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

# def index():
#     return "<h1>Hello World!</h1>"

def index():
    first_name = "Mineth"
    stuff = "This is Bold Text"

    favorite_pizza = ["Pepperoni","Cheese","Jalapenos",32]
    return render_template("index.html",first_name = first_name,stuff= stuff,favorite_pizza = favorite_pizza)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html",user_name = name)


# creating custom error pages

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(505)
def page_not_found(e):
    return render_template("505.html"), 505