from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='color:purple;'>Сошина Ксения Викторовна 44-24-232 Практика 07</h1>"

@app.route("/02")
def route02():
    return render_template ("02/index.html")

@app.route("/03")
def route03():
        return render_template ("03/index-bootstrap.html")