from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Бобкова Кристина Сергеевна гр. 44-24-229</p>"
@app.route("/02")
def ha02():
    return render_template("02/index.html")
@app.route("/03")
def ha02():
    return render_template("03/index.html")
@app.route("/task/<stone>")
def task(stone):
    jewels = "pgs"
    count = 0
    for s in stone:
        if s in jewels:
            count+=1
    return f"Вы нашли {count} драгоценных камней, поздравляем!!!!"    