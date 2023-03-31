# Importing modules
from flask import Flask, render_template

# Making the app
app = Flask(__name__)


# When on the home page run this function
@app.route("/")
def home(name=None):
    return render_template("index.html", name=name)


# If name is equal to "__main__" then run the app
if __name__ == "__main__":
    app.run(debug=True)
