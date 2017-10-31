# -*- coding:utf8 -*-
'''
User Form.
'''
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo, ValidationError
from ..models import User, Role
from flask_pagedown.fields import PageDownField

class CommentForm(Form):
    comment = PageDownField('记录你的声音', validators=[Required()])
    submit = SubmitField('提交')
