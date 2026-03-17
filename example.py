
from flask import Flask 
from markupsafe import escape

app = Flask(__name__) 

@app.route("/") 
def hello_world(): 
    name = {"name":"eric", "natioality":"Ugandan"}
    return escape("<h1> hello</h1>")

@app.route("/user/<int:id>")
def user(id):

    users = [{
        "name": "eric",
        "age": 41
    },
    
    {
        "name": "Kevin",
        "age": 20
    }
    ]

    # Logic to loop through the list and return a user based on the index.

    for i in users:
        return f'{users[id]["name"]} : {users[id]["age"]}'

    # return f"hello from about :{name}"














@app.route("/about", methods=["GET"])
def about():
    return "about"

from flask import request

users = [] # like our database

@app.route("/articles/create", methods=["POST", "GET"])
def articles():
    # We need to grab user input and then post somewhere to the database
    # To grab the data we need to access the request..

    # Grab a request from the user
    if request.method == "POST":
        user = {
            "name": request.form["name"],
            "email": request.form["email"]
        }
        # logic to send the user the database.. 

        users.append(user)
        return users

    if request.method == "GET":
        return "===✨Hello, we are here=== "

