# -*- coding:utf8 -*-
'''
Main Form.
'''
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo, ValidationError
from ..models import Post
from flask_pagedown.fields import PageDownField
import re

class PostForm(Form):
    title = StringField('博文标题', validators=[Required(), Length(0, 120)])
    tags = StringField('博文标签', validators=[Required(), Length(0,120)])
    body = PageDownField('有什么好的想法？', validators=[Required()])
    submit = SubmitField('提交')

    def validate_tags(self, filed):
        regx = r'^[0-9a-zA-Z;\u4E00-\u9FA5]*$'
        pattern = re.compile(regx, re.S)
        if pattern.match(filed.data) == None:
            raise ValidationError('标签栏只包含英文单词、汉子和半角；。')
        tag_list = filed.data.split(';')
        for tag in tag_list:
            if len(tag) > 10:
                raise ValidationError('单个标签长度不得大于10字节。')
