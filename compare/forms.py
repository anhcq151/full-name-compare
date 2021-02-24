from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class inputForm(FlaskForm):
    original_list = TextAreaField(label='Danh sách hành khách cần đổi tên', validators=[DataRequired(message="Danh sách không được bỏ trống!")])
    change_list = TextAreaField(label='Danh sách tên hành khách sau khi đổi', validators=[DataRequired(message="Danh sách không được bỏ trống!")])
    submit = SubmitField(label='So sánh')