from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired

class ResultForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    score = FloatField('Score', validators=[DataRequired()])
    student_id = SelectField('Student', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Add Result')
