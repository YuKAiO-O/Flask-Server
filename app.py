from flask import Flask, request, redirect, url_for, render_template, make_response

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"