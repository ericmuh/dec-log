from flask import Flask, render_template

app = Flask(__name__)

decisions = [
    {
        "title": "Use Flask for the Decision Log project",
        "reason": "It is lightweight and beginner-friendly",
    },
    {
        "title": "Start with server-rendered pages",
        "reason": "Build core Flask understanding before APIs",
    },
]


@app.route("/")
def home():
    return render_template("index.html", decisions=decisions)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
