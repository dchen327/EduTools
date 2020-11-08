from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length

class AnnouncementForm(FlaskForm):
    message = TextAreaField('Announcement Message:', [
        DataRequired()])
    recipient = SelectField(u'Send To:', choices=[('All Students'),('Daniel Li'),('David Chen')])
    submit = SubmitField('Submit')
    