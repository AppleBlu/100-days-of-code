# Importing modules
from flask import Flask
import random

# App is the Flask with the name of the file
app = Flask(__name__)


# When the user is on the home page run this function
@app.route("/")
def instruction():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media1.giphy.com/media/l378khQxt68syiWJy/giphy." \
           "gif?cid=ecf05e47tvhnxd8lvz73hpmd5spcw1zcpgyx4nsu4x26z6n3&rid=giphy.gif&ct=g'>"


# Generating a random number between 0 and 9
random_number = random.randint(0, 9)


@app.route("/<int:guess>")
def guess_number(guess):
    if guess == random_number:
        return "<h1 style='background-color:green;'>You got it!!!</h1>" \
               "<img src='https://media1.giphy.com/media/Pnb5GTXdF54QxEaiLZ/200w.webp?cid=ecf05e479m9soi6zkmk2h414smd" \
               "00tnd8w9d02tczcm1r204&rid=200w.webp&ct=g'>"
    elif guess < random_number:
        return "<h1 style='background-color:red;'>Too low sorry</h1>" \
               "<img src='https://media1.giphy.com/media/R5unorzb9UtmrAPpl7/200w.webp?cid=ecf05e473ynr13p3mcccmrppdpx" \
               "lhepmqfjrcum82udugujd&rid=200w.webp&ct=g'>"
    else:
        return "<h1 style='background-color:red;'>Too high</h1>" \
               "<img src='https://media2.giphy.com/media/oiGCnybFPh6Q8/200w.webp?cid=ecf05e47zib9qw0atf17ygdxlotwfq0" \
               "e35sye9i2tdg23kwb&rid=200w.webp&ct=g'>"


# If name of the current file is "__main__" then run the app
if __name__ == "__main__":
    app.run(debug=True)
