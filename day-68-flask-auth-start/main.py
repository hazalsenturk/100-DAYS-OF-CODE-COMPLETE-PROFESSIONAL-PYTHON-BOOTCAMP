import werkzeug
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'j^60*hf-6ms/w#sn1!mk"co'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        if User.query.filter_by(email=request.form.get('email')).first():
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hashed_and_slated_password = generate_password_hash(
            request.form['password'],
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hashed_and_slated_password
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        return render_template("secrets.html", name=new_user.name.title())
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form.get('email')
        password_given = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("That email does not exist, please try again. ")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password_given):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        # Email exists and password correct
        else:
            login_user(user)
            return redirect(url_for('secrets'))
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', filename='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)