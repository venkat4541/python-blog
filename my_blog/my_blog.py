from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('home.html')

@app.route('/about')
def about():
    return app.send_static_file('about.html')

@app.route('/contact')
def contact():
    return app.send_static_file('contact.html')

@app.route('/post/1')
def post1():
    return 'This is post 1'

@app.route('/post/<postnum>')
def post(postnum):
    return 'This is post' + postnum
