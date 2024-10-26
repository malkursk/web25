from flask import Flask, render_template, redirect, url_for
from models import db, Student, Result
from forms import ResultForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///results.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  

db.init_app(app)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add_result', methods=['GET', 'POST'])
def add_result():
    form = ResultForm()
    if form.validate_on_submit():
        new_result = Result(
            subject=form.subject.data,
            score=form.score.data,
            student_id=form.student_id.data
        )
        db.session.add(new_result)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_result.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
