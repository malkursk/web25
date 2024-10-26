# pip install Flask
# flask --app app run --debug

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Привет!!!"

@app.route("/1/<v>")
def f1(v):
    return render_template("/01/index.html", name=v)

@app.route("/2")
def f2():
    return render_template("/02/index.html")

@app.route("/calc/<int:a>/<int:b>")
def fcalc(a,b):
    return a+b
