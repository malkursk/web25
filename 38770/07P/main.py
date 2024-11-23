from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def route01():
    return "<p>Практическая работа 7.<h1> Чиненова Алина Александровна, </h1> 44-24-232</p>"

@app.route("/02")
def route02():
    return render_template ("02/index.html")

@app.route("/03")
def route03():
    return render_template ("03/index.html")

@app.route("/calc/<a>/<b>")
def calc(a,b):
    return f"{int(a)**5+int(b)**10}"