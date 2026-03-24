from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

# Root route → Home page
@app.route("/")
def index():
    return render_template("index.html")

# Join page route → handles form
@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        association = request.form.get("association")
        interest = request.form.get("interest")
        message = request.form.get("message")

        if not name or not email:
            flash("Please fill in all required fields.", "error")
            return redirect(url_for("join"))

        print(f"New submission: {name}, {email}, {association}, {interest}, {message}")
        flash("Thanks! Your message has been sent.", "success")
        return redirect(url_for("join"))

    return render_template("join.html")

# Other static pages
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/events")
def events():
    return render_template("events.html")

if __name__ == "__main__":
    app.run(debug=True)