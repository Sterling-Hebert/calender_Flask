from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, TimeField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    start_date = DateField("Start Date", format='%Y-%m-%d')
    start_time = TimeField("Start Time", format='%H:%M')
    end_date = DateField("End Date", format='%Y-%m-%d')
    end_time = TimeField("End Time", format='%H:%M')
    description = TextAreaField("Description", validators=[DataRequired()])
    private = BooleanField("Private?")
    submit = SubmitField("Submit")
