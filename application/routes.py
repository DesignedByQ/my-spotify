from application import app
from application import db
from application.models import Playlist, Songs
from flask import redirect, url_for, render_template, request


@app.route('/db')
def dbcon():
    todo = 'Connected'
    return todo

@app.route('/')
@app.route('/home')
def home():
    intro = "Welcome to My-Spotify, please select from the options below"
    #hyperlink to songs db or pls
    return intro

#shows all the songs in the db
@app.route('/songs')
def songs():
    all_songs = Songs.query.all()
    return render_template('songs.html', songslist=all_songs)


@app.route('/read')
def read():
    all_pl = Playlist.query.all()
    pl_string = ""
    for pl in all_pl:
        pl_string += "<br>"+ pl.title + " " + str(pl.count)
    return pl_string

@app.route('/sing')
def sing():
    all_sg = Songs.query.all()
    sg_string = ""
    for sg in all_sg:
        sg_string += "<br>" + sg.title + "/" + sg.artist + "/" + sg.feature + "/" + sg.category + "/" + sg.reldate + "/" + sg.length + "/" + sg.playlist_title + "<br>"
    return sg_string

