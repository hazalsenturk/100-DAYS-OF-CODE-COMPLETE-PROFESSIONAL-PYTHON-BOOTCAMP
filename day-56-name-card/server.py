# DO NOT USE THIS WEBSITE_ MESSED UP THE STYLES :) \
# TO MOVE OON PICK ANOTHER TEMPLATE:  https://html5up.net AND START OVER

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
