'''
MSc Computer Systems and Management
CSTM65 Software Engineering Principles
Author: Paul Jones
Date: 20/10/2020

Week 7 - Creating a basic web app with front end/backend 
'''
from flask import Flask, render_template, request, redirect
from Rivers import *
from array import *
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

RiverID = 0
NewRiverList = []

def Add_River(rivername, length, Miles, RiverRating):
     global RiverID
     NewRiver = [RiverID, rivername, length, Miles, RiverRating]
     NewRiverList.append(NewRiver)  
     RiverID += 1


# Flask routes support GET requests by default.
# However it must be declared if the methods argument is provided.
@app.route("/river", methods=["GET", "POST"])
def New_River():

    if request.method == "POST":

        req = request.form
        rivername = req.get("rivername")
        length = req.get("length")
        rapids = req.get("rapids")

        
        description = (f"\nRiver name is: {rivername}\n"
                       f"Length is: {length}km\n"
                       f"Rapids are Grade {rapids}\n")
        
        print(description)

        MissingFields = list()

        for DicKey, DicValue in req.items():
            if DicValue == "":
                MissingFields.append(DicKey)

        if MissingFields:
            feedback = f"Missing fields for {', '.join(MissingFields)}"
            return render_template("river.html", feedback=feedback)
        else:        
            rapids = int(rapids)
            length = int(length)
            Miles = Km_To_Miles(length)
            RiverScore = Rating(length, rapids)
            RiverRating = River_Grade(RiverScore)
            Add_River(rivername, length, Miles, RiverRating)
        print(Miles)
        print(RiverScore)
        print(RiverRating)
        print(NewRiverList[0])
        render_template("results.html", rivers = NewRiverList)

    return render_template("river.html")


@app.route("/results", methods=["GET", "POST"])
def View_River_Details():
    print(request.method)
    if request.method =='POST':
        print("inside")
        print(request.method)
        if request.form['Display'] == 'Display':
            return render_template("results.html", rivers = NewRiverList)
    
    return render_template("results.html")


app.run(debug=True)
