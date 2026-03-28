from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///decisions.db"


# Definiing the DB ( instance of SQLAlchemy and attaching our app)
db = SQLAlchemy(app)


# A Model --> defines a table in our SQL database
class Decision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    reason = db.Column(db.String(120))
    confidence_level = db.Column(db.Integer)
    outcome = db.Column(db.String)
    lesson = db.Column(db.Text)
    create_at = db.Column(db.DateTime)


with app.app_context():
    db.create_all()


# =============================================

# VIEWS
# =============================================


# Would a place to see all decision (lists all decions)
@app.route("/")
@app.route("/decisions")
def decisions():

    # logic to retrieve all decision from the database
    decisions = Decision.query.all()

    return render_template("home.html", decisions=decisions)


# Reading a Single Decsions
@app.route("/decisions/<int:id>")
def single_decision(id):

    decision = Decision.query.get_or_404(id)
    return render_template("single_decision.html", decision=decision)


# Create a decision
@app.route("/create", methods=["GET", "POST"])
def create_decision():
    if request.method == "POST":

        # creating a new row in out Decision table
        decision = Decision(
            title=request.form["title"],
            reason=request.form["reason"],
            confidence_level=request.form["confidence_level"],
        )

        # commiting the changes to the table
        db.session.add(decision)
        db.session.commit()
        return redirect(url_for("decisions"))

    return render_template("create_decision.html")


# Update A decision
@app.route("/decisions/update/<int:id>", methods=["GET", "POST"])
def update_decision(id):

    # get a specific decision in the list using the index,
    decision = Decision.query.get_or_404(id)

    # get the details from the form
    # TODO: Fix this for update
    if request.method == "POST":

        # updating the decision based on existing data
        decision.title=request.form["title"]
        decision.reason=request.form["reason"]
        decision.confidence_level=request.form["confidence_level"]
        decision.outcome=request.form["outcome"]
        decision.lesson_learned=request.form["lesson_learned"]
        

        # commiting the changes to the table
        db.session.commit()

        print(decision)

        return redirect(url_for("decisions"))

    return render_template(
            "update_decision.html", decision=decision,
        )


# Delete a Decision : STANDALONE as we don't have to render a template ( use in the single decision template)
@app.route("/decisions/delete/<int:id>", methods=["POST"])
def delete_decision(id):
    decision = Decision.query.get_or_404(id)
    db.session.delete(decision)
    db.session.commit()
    return redirect(url_for("decisions"))


if __name__ == "__main__":
    app.run(debug=True)
