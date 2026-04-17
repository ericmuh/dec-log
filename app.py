from datetime import date

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# In-memory sample data for this lesson stage.
decisions = [
    {
        "id": 1,
        "title": "Invest in Bitcoin",
        "reason": "Good market trends",
        "confidence_level": 3,
        "outcome": "Pending",
        "lesson": "Watch volatility signals before acting",
        "created_at": "2026-03-09",
    },
    {
        "id": 2,
        "title": "Work Out",
        "reason": "Get in shape",
        "confidence_level": 5,
        "outcome": "Success",
        "lesson": "Consistency beats motivation",
        "created_at": "2026-03-10",
    },
    {
        "id": 3,
        "title": "Launch study routine",
        "reason": "Build daily momentum",
        "confidence_level": 4,
        "outcome": "Pending",
        "lesson": "Schedule blocks in advance",
        "created_at": "2026-03-11",
    },
]


def find_decision(decision_id):
    return next((d for d in decisions if d["id"] == decision_id), None)


def parse_confidence(raw_value, fallback):
    try:
        value = int(raw_value)
    except (TypeError, ValueError):
        return fallback

    return value if 1 <= value <= 5 else fallback


@app.route("/")
def home():
    return render_template("index.html", decisions=decisions)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/decisions/new", methods=["GET", "POST"])
def create_decision():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        reason = request.form.get("reason", "").strip()
        confidence_level = parse_confidence(request.form.get("confidence_level"), 3)
        outcome = request.form.get("outcome", "Pending").strip() or "Pending"
        lesson = request.form.get("lesson", "").strip() or "No lesson recorded yet"

        if title and reason:
            new_id = max((d["id"] for d in decisions), default=0) + 1
            decisions.append(
                {
                    "id": new_id,
                    "title": title,
                    "reason": reason,
                    "confidence_level": confidence_level,
                    "outcome": outcome,
                    "lesson": lesson,
                    "created_at": date.today().isoformat(),
                }
            )
            return redirect(url_for("decision_detail", decision_id=new_id))

    return render_template("create_decision.html")


@app.route("/decisions/<int:decision_id>/edit", methods=["GET", "POST"])
def edit_decision(decision_id):
    decision = find_decision(decision_id)
    if decision is None:
        return render_template("not_found.html", decision_id=decision_id), 404

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        reason = request.form.get("reason", "").strip()
        confidence_level = request.form.get("confidence_level", "").strip()
        outcome = request.form.get("outcome", "").strip()
        lesson = request.form.get("lesson", "").strip()

        if title:
            decision["title"] = title
        if reason:
            decision["reason"] = reason
        if confidence_level:
            decision["confidence_level"] = parse_confidence(
                confidence_level, decision["confidence_level"]
            )
        if outcome:
            decision["outcome"] = outcome
        if lesson:
            decision["lesson"] = lesson

        return redirect(url_for("decision_detail", decision_id=decision_id))

    return render_template("edit_decision.html", decision=decision)


@app.route("/decisions/<int:decision_id>")
def decision_detail(decision_id):
    decision = find_decision(decision_id)
    if decision is None:
        return render_template("not_found.html", decision_id=decision_id), 404

    return render_template("decision_detail.html", decision=decision)


@app.route("/decisions/<int:decision_id>/delete", methods=["POST"])
def delete_decision(decision_id):
    decision = find_decision(decision_id)
    if decision is None:
        return render_template("not_found.html", decision_id=decision_id), 404

    decisions.remove(decision)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
