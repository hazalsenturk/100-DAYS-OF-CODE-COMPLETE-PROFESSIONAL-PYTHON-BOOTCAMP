from flask import Flask
import random

app = Flask(__name__)

def homey(function):
    def wrapper():
        return f'<h1>{function()} \n</h1>' \
               '<img src="https://media.giphy.com/media/LPrkJEtF24P0HHZL8t/giphy.gif" width=200>'
    return wrapper

@app.route('/')
@homey
def home_page():
    return 'Guess a number between 0 and 9.'

rand_number = random.randint(1,10)
print(rand_number)

@app.route('/<int:number>')
def check_number(number):
    if number == rand_number:
        return '<h1 style="color:blue;"> You found it! </h1>'\
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=200>'
    elif number < rand_number:
        return '<h1 style="color:green;"> Too low! </h1>'\
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=200>'
    elif number > rand_number:
        return '<h1 style="color:red;"> Too high! </h1>'\
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=200>'

if __name__ == "__main__":
    app.run(debug=True)
