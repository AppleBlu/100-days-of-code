# Importing modules
from flask import Flask, render_template
from post import Post

# Creating a flask app
app = Flask(__name__)

# Initialising the class Post
post = Post()


# When on the home root of the website run this function
@app.route('/')
def home(name=None):
    # Rending the index template with the kwarg blog_data passed in
    return render_template("index.html", name=name, posts=post.blog_data)


# When on /blog/(id of the blog) run this function
@app.route("/blog/<int:id>")
def full_blog_post(id):
    return render_template("post.html", posts=post.blog_data, id=id)


# If __name__ is equal to __main__ then run the flask app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
