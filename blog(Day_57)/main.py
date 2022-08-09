from flask import Flask, render_template
from post import Post
import requests


app = Flask(__name__)


@app.route('/')
def home():
    all_posts = get_all_post()
    return render_template("index.html", all_posts=all_posts)


@app.route('/post/<int:id>')
def get_post_by_id(id):
    post = get_post(id)
    return render_template('post.html', post=post)


def get_all_post():
    r = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = []
    for i in r.json():
        post = Post(i["id"], i["title"], i["subtitle"], i["body"])
        all_posts.append(post)
    return all_posts


def get_post(id_):
    r = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = r.json()
    for i in all_posts:
        if i["id"] == id_:
            post = Post(i["id"], i["title"], i["subtitle"], i["body"])
            return post


if __name__ == "__main__":
    app.run(debug=True)
