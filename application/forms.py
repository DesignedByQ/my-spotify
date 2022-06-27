from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired

class SongForm(FlaskForm):
    ntitle = StringField('Song Title', validators=[DataRequired()])
    nartist = StringField('Artist', validators=[DataRequired()])
    nfeature = StringField('Feature')
    ncategory = StringField('Category', validators=[DataRequired()])
    nreldate = DateField('Release Date', validators=[DataRequired()])
    nlength = StringField('Length', validators=[DataRequired()])
    submit = SubmitField('Add Song')

class UpdateForm(FlaskForm):
    otitle = StringField('Old Song Title', validators=[DataRequired()])
    ntitle = StringField('New Song Title', validators=[DataRequired()])
    oartist = StringField('Old Artist', validators=[DataRequired()])
    nartist = StringField('New Artist', validators=[DataRequired()])
    ofeature = StringField('Old Feature')
    nfeature = StringField('New Feature')
    ocategory = StringField('Old Category', validators=[DataRequired()])
    ncategory = StringField('New Category', validators=[DataRequired()])
    oreldate = DateField('Old Release Date', validators=[DataRequired()])
    nreldate = DateField('New Release Date', validators=[DataRequired()])
    olength = StringField('Old Length', validators=[DataRequired()])
    nlength = StringField('New Length', validators=[DataRequired()])
    submit1 = SubmitField('Update Song')