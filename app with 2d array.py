'''
MSc Computer Systems and Management
CSTM65 Software Engineering Principles
Author: Paul Jones
Date: 20/10/2020

Week 7 - Creating a basic web app with front end/backend 
'''
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

UserID = 0
NewUsers = dict()


def Add_User(Name, Email, Pass):
     global UserID
     NewUsers = {UserID : {Name, Email, Pass}}   
     UserID += 1
     print(UserID)
     
# Flask routes support GET requests by default.
# However it must be declared if the methods argument is provided.
@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form
        username = req.get("username")
        email = req["email"]
        password = request.form["password"]

        description = (f"\nUsername is: {username}\n"
                       f"Email is: {email}\n"
                       f"Password is: {password}\n")
        
        print(description)

        MissingFields = list()

        for DictKey, DictValue in req.items():
            if DictValue == "":
                MissingFields.append(DictKey)

        if MissingFields:
            feedback = f"Missing fields for {', '.join(MissingFields)}"
            return render_template("sign_up.html", feedback=feedback)

        Add_User("username", "email", "password")
        return redirect(request.url)
        
    return render_template("sign_up.html")


app.run(debug=True)


