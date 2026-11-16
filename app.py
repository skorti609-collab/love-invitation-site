
from flask import Flask, render_template, request, redirect, session
from datetime import date

app = Flask(__name__)
app.secret_key = "love-invitation-secret-key-2026"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/place", methods=["POST"])
def place():
    selected_date = request.form.get("date", "")
    try:
        chosen = date.fromisoformat(selected_date)
        if not date(2026, 11, 26) <= chosen <= date(2026, 12, 5):
            return "Пожалуйста, выбери дату с 26 ноября по 5 декабря.", 400
    except ValueError:
        return "Выбери правильную дату.", 400

    session["date"] = selected_date
    return render_template("place.html", chosen_date=selected_date)

@app.route("/thanks", methods=["POST"])
def thanks():
    place = request.form.get("place", "")
    if place not in ["KFC", "McDonald's", "Суши дома"]:
        return redirect("/")
    if "date" not in session:
        return redirect("/")

    session["place"] = place
    return render_template(
        "thanks.html",
        chosen_date=session["date"],
        place=place
    )

if __name__ == "__main__":
    app.run()
