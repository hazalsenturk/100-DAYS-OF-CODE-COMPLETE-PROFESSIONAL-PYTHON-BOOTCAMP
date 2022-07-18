from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = "testpython.g21@gmail.com"
MY_PASSWORD = "cexjyj-3cawvu-vavseH"

app = Flask(__name__)

all_posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/<title>/<int:int_id>')
def post_page(title, int_id):
    for post_single in all_posts:
        if title == post_single['title'] and int_id == int(post_single['id']):
            current_post = post_single
    return render_template("post.html", post=current_post)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        email_msg = f"Subject:New Message\n\nName: {data['name']}\nEmail: {data['email']}\nPhone:{data['phone']}\n" \
                    f"Message:{data['message']}".encode('utf-8')
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=email_msg)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)