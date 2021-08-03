from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/products')
def products():


    return render_template("products.html")


@app.route('/total')
def total():
    return render_template("total.html")
