# Importing modules
import flask
from flask import Flask, render_template

# Creating an app using flask
app = Flask(__name__)


# When on the home page run this function
@app.route("/")
def home(name=None):
    return render_template("index.html", name=name)


# If name of the current file is "__main__" then run the app (By adding debug true I can edit the file, and it updates
# the website live without be having to reset it manually) I have to hit save after updating
if __name__ == "__main__":
    app.run(debug=True)
