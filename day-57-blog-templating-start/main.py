from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    BLOG_URL = "https://api.npoint.io/5abcca6f4e39b4955965"
    ALL_POSTS = requests.get(BLOG_URL).json()
    return render_template("index.html", posts=ALL_POSTS)


@app.route("/blog/<int:num>")
def get_blog(num):
    BLOG_URL = "https://api.npoint.io/5abcca6f4e39b4955965"
    ALL_POSTS = requests.get(BLOG_URL).json()
    return render_template("post.html", num=num, posts=ALL_POSTS)

if __name__ == "__main__":
    app.run(debug=True)
