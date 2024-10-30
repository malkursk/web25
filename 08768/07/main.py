from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return "<p style='color:green'>Беляева А.А. 44-24-230</p>"

@app.route("/03")
def route3():
    return render_template("03/index.html")

@app.route("/02")
def route2():
    return render_template("02/index.html")

@app.route("/task/<stone>")
def task(stone):
    jewels="pgs"
    count=0
    for s in stone:
        if s in jewels:
            count+=1
    return f"вы нашли {count} драгоценных камней"