from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime as dt


# Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# CONFIGURE TABLE


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = BlogPost.query.filter_by(id=index).first()
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/edit-post/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    form = CreatePostForm(obj=post)
    if request.method == "POST":
        if check_title(form.title.data, post_id):
            return jsonify({"error": "This title is existed"})
        else:
            post.title = form.title.data
            post.subtitle = form.subtitle.data
            post.author = form.author.data
            post.img_url = form.img_url.data
            post.body = form.body.data
            try:
                db.session.commit()
            except Exception as error:
                db.session.rollback()
            return redirect(url_for('show_post', index=post_id))
    return render_template('make-post.html', form=form)


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()
    if request.method == "POST":
        if check_title(form.title.data):
            return jsonify({"error": "This title is existed"})
        else:
            post = BlogPost()
            post.title = form.title.data
            post.subtitle = form.subtitle.data
            post.date = dt.today().strftime("%B %-d,%Y")
            post.body = form.body.data
            post.author = form.author.data
            post.img_url = form.img_url.data
            db.session.add(post)
            try:
                db.session.commit()
            except Exception as error:
                db.session.rollback()
            return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)


def check_title(title, post_id=None):
    """
    check title is existed or not
    post_id is not necessary when add a new post
    """
    post = BlogPost.query.filter_by(title=title).first()
    if post:
        if post_id is None:
            return True
        else:
            if post.id == post_id:  # users can edit the post without editing the title
                return False
            return True
    return False


@app.route('/delete/<int:post_id>')
def delete(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
