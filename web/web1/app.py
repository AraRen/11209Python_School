from flask import Flask,url_for,render_template
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    name = "AraRen"
    age = 26
    return render_template('index.html',name=name,age=age)

@app.route("/hello")
def hello():
    return "hello world"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id*5}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {subpath}'

@app.route('/url')
def url():
    print(url_for('hello'))
    print(url_for('show_user_profile',username="CBA"))
    print(url_for('static',filename="css/style.css"))
    return "ABC"