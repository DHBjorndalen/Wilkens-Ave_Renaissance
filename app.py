import os
import csv
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from wtforms import SelectField

load_dotenv() 

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev_key") 
csrf = CSRFProtect(app) 

# ---------------------
# Flask-WTF Form
# ---------------------
class JoinForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=50)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    association = StringField("Association", validators=[Length(max=100)])
    interest = SelectField(
        "How would you like to get involved?",
        choices=[
            ("", "— Select one —"),
            ("email_updates", "Stay informed via email updates"),
            ("monthly_meetings", "Attend monthly meetings"),
            ("volunteer", "Volunteer at events"),
            ("outreach", "Help with outreach & communications"),
            ("represent_block", "Represent my block or organization"),
            ("other", "Other — I'll explain below"),
        ]
    )
    message = TextAreaField("Message", validators=[Length(max=500)])
    submit = SubmitField("Submit")

# ---------------------
# Routes
# ---------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/join", methods=["GET", "POST"])
def join():
    form = JoinForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        association = form.association.data
        interest = form.interest.data
        message = form.message.data

        # Save to CSV
        csv_path = os.path.join(os.path.dirname(__file__), "submissions.csv")
        file_exists = os.path.isfile(csv_path)
        with open(csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Name", "Email", "Association", "Interest", "Message"])  # header
            writer.writerow([name, email, association, interest, message])

        flash("Thanks! Your message has been sent.", "success")
        return redirect(url_for("join"))

    return render_template("join.html", form=form)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/events")
def events():
    return render_template("events.html")

if __name__ == "__main__":
    app.run()