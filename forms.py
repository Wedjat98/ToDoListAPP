from __future__ import unicode_literals
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length


class TodoListForm(FlaskForm):
    title = StringField('ToDo内容', validators=[DataRequired(), Length(1, 64)])
    status = RadioField('是否完成', validators=[DataRequired()], choices=[("1", '已完成'), ("0", '未完成')])
    submit = SubmitField('提交')


class LoginForm(FlaskForm):
    username = StringField('用户', validators=[DataRequired(), Length(1, 24)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 24)])
    submit = SubmitField('登录')
