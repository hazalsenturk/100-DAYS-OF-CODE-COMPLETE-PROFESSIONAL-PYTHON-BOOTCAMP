from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    gender = requests.get(url=f"https://api.genderize.io?name={name}").json()["gender"]
    age = requests.get(url=f"https://api.agify.io?name={name}").json()["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    all_posts = requests.get(blog_url).json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)

