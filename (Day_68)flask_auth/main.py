from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin, db.Model):  # multiple inheritance
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    salt = db.Column(db.String(50))
# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if check_email(request.form["email"]):
            flash("You have already signed up with that email.Please sign in.")
            return render_template("register.html")
        else:
            user = User()
            user.name = request.form["name"]
            user.email = request.form["email"]
            encrypted_str = generate_password_hash(  # encrypt password
                request.form["password"], method='pbkdf2:sha256', salt_length=8)
            user.password = encrypted_str.split('$')[2]
            user.salt = encrypted_str.split('$')[1]
            db.session.add(user)
            try:
                db.session.commit()
                login_user(user)  # automatic login after registration
            except Exception as error:
                db.session.rollback()
            return redirect(url_for('home'))
    return render_template("register.html")


def check_email(email):
    email = User.query.filter_by(email=email).first()
    if email:
        return True
    else:
        return False


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user:
            pwhash = 'pbkdf2:sha256:260000' + '$' + user.salt + '$' + user.password
            if check_password_hash(pwhash, password):
                login_user(user)
                return render_template("secrets.html")
            else:
                flash("Password incorrect.Please try again.")
                return render_template("login.html")
        else:
            flash('The email does not exist.Please try again.')
            return render_template("login.html")
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        'static/files',  # don't put / at the beginning
        'cheat_sheet.pdf')


@login_manager.user_loader
def user_loader(user_id):  # the parameter must be user.id
    user = User.query.get(user_id)
    return user if user else None


if __name__ == "__main__":
    app.run(debug=True, port=5001)
