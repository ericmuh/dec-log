from flask import Flask, render_template,request

app = Flask(__name__)

# this will act as our database ( A list of python dictionaries)
decisions = [
    {
        "id": 0,
        "title": "Invest in Bitcoin",
        "reason": "Market trend looked strong and many analysts predicted growth",
        "confidence_level": "3",
        "outcome": "Price dropped shortly after investment",
        "lesson_learned": "Avoid investing based only on hype, do deeper research",
        "created_at": "2026-03-01"
    },
    {
        "title": "Start a Flask teaching project",
        "reason": "Students learn better by building real applications",
        "confidence_level": "2",
        "outcome": "Students engaged more and asked deeper questions",
        "lesson_learned": "Hands-on projects improve understanding significantly",
        "created_at": "2026-03-02"
    },
    {
        "id": 2,
        "title": "Wake up at 5 AM daily",
        "reason": "More quiet time for focused work",
        "confidence_level": "5",
        "outcome": "Productivity improved in the mornings",
        "lesson_learned": "Morning routines can significantly increase focus",
        "created_at": "2026-03-03"
    },
    {
        "id": 3,
        "title": "Buy a second monitor",
        "reason": "Coding and teaching would be easier with more screen space",
        "confidence_level": "4",
        "outcome": "Workflow became faster and more organized",
        "lesson_learned": "Small hardware upgrades can greatly improve productivity",
        "created_at": "2026-03-05"
    },
    {
        "id": 4,
        "title": "Use Excalidraw for teaching diagrams",
        "reason": "It is simple, visual, and good for explaining systems",
        "confidence_level": "5",
        "outcome": "Students understood system architecture faster",
        "lesson_learned": "Visual tools improve comprehension for complex topics",
        "created_at": "2026-03-07"

    }
]

# structure of a single decision ( so far this does nothing)
decision = {
"ID":"", # interger
"title": "", # text
"reason": "", # text
"confidence level":"", # interger
"outcome": "", #text
"lesson": "" , #text
"created_at": "" #date  
}














# Views

# Would a place to see all decision (lists all decions)
@app.route("/")
@app.route("/decisions")
def decisons():

    # logic to retrieve all decision from the database


    return render_template("home.html", decisions=decisions)




# Reading a Single Decsions
@app.route("/decisions/<int:id>")
def single_decision(id):
    # rendered_decision = None
    for decision in decisions:
        # rendered_decision = decisions[id]
        return render_template("single_decision.html", decision=decisions[id])





# Create a decision
@app.route("/create", methods=["GET", "POST"])
def create_decision():
    if request.method=="POST":
        # logic to create a decision
        
       decision = {
        "title": request.form["title"],
        "reason": request.form["reason"],
        "confidence_level": request.form["confidence_level"],}
       decisions.append(decision)


       print ("We Have posted ✨🧪", decisions)

    return render_template("create_decision.html", decisions=decisions)


@app.route("/decisions/update/<int:id>", methods = ["GET", "POST"])
def update_decision(id):

    # get a specific decision in the list using the index,
    # remove that decision, : option 2 --> point the index to the new decision
    # add the new decision
    if request.method =="POST":
        update_decision = {
            "title": request.form["title"],
            "reason": request.form["reason"],
            "confidence_level": request.form["confidence_level"],
            
            "outcome": request.form["outcome"],
            "lesson_learned": request.form["lesson_learned"],

            }
    
        decisions[id] = update_decision
        print(decisions)

    decision = ''
    for decision in decisions:
        # rendered_decision = decisions[id]
        return render_template("update_decision.html", decision=decisions[id], id=id, decisions=decisions)













# Connecting to a database using sqlite3
import sqlite3

db = sqlite3.connect("database.db") # use in SQL

cursor = db.cursor()


# cursor.execute("CREATE TABLE decisions(title, reason, confidence_level,outcome, lesson_learned)")






if __name__ =="__main__":
    app.run(debug=True)