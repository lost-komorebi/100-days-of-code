from flask import Flask, render_template, redirect
from forms import MyForm
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = "DlE3et4UOYD3HWo6rJaA8uxSbSCdRySO"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        email = form.email.data
        pwd = form.password.data
        if email == "admin@email.com" and pwd == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
