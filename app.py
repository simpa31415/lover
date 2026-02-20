from flask import Flask, render_template

# Skapa Flask-appen
app = Flask(__name__)

# Route för startsidan
@app.route("/")
def home():
    return render_template("index.html")