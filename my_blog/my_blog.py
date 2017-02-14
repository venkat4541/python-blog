from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'May 17 1990'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' + name + '!'
