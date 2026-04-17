from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

# Sample in-memory data for this lesson.
decisions = [
    {
        "id": 1,
        "title": "Adopt weekly planning",
        "reason": "Improve team coordination",
        "confidence_level": 8,
    },
    {
        "id": 2,
        "title": "Use Flask templates first",
        "reason": "Learn core web concepts before APIs",
        "confidence_level": 9,
    },
]


@app.route("/")
def home():
    return render_template("index.html", decisions=decisions)


@app.route("/about")
def about():
    return render_template("about.html")


# Dynameic route with an integer parameter. This route will display the details of a specific decision based on its ID. If the decision is not found, it will return a 404 page.
@app.route("/decisions/<int:decision_id>")
def decision_detail(decision_id):
    for decision in decisions:
        if decision["id"] == decision_id:
            return render_template("decision_detail.html", decision=decision)

    return (
        render_template("not_found.html", decision_id=decision_id),
        404,
    )  # if decision is not found, return 404 page


# Example of a dynamic route with a string parameter.( creating a member profile page that takes a username as a parameter)
@app.route("/member/<string:username>")
def member_profile(username):
    return render_template("member_profile.html", username=username)


# The route returen a redirect response to the home page when the user visits /go-home. This demonstrates how to use Flask's redirect and url_for functions to navigate between routes.
@app.route("/go-home")
def go_home():
    return redirect(url_for("home"))


# custom 404 error handler that renders a user-friendly page when a requested resource is not found. This enhances the user experience by providing informative feedback instead of a generic error message.
@app.errorhandler(404)
def page_not_found(e):
    return render_template("not_found.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
