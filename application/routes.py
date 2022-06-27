from application import app
from application import db
from application.models import Playlist, Songs
from flask import redirect, url_for, render_template, request
from application.forms import SongForm, UpdateForm


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

#add song to the db
@app.route('/add', methods=['GET', 'POST'])
def add():
    message = ""
    form = SongForm()

    if request.method == 'POST':
        ntitle = form.ntitle.data
        nartist = form.nartist.data
        nfeature = form.nfeature.data
        ncategory = form.ncategory.data
        nreldate = form.nreldate.data
        nlength = form.nlength.data
        message = ntitle + ' has been added'

        if ntitle:
            new_song = Songs(title=ntitle, artist=nartist, feature=nfeature, category=ncategory, reldate=nreldate, length=nlength)
            db.session.add(new_song)
            db.session.commit()  

    return render_template('add.html', form=form, message=message)

#delete song
@app.route('/delete/<int:id>')
def delete(id):
    to_be_del = Songs.query.get(id)
    db.session.delete(to_be_del)
    db.session.commit()
    return redirect(url_for('songs'))

#update song
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    message = ""
    form = UpdateForm()

    toupdate = Songs.query.get(id)

    if form.validate_on_submit():
        toupdate.title = form.ntitle.data
        toupdate.artist = form.nartist.data
        toupdate.feature = form.nfeature.data
        toupdate.category = form.ncategory.data
        toupdate.reldate = form.nreldate.data
        toupdate.length = form.nlength.data
        db.session.commit()
        message = form.otitle.data + ' has been updated'
        #return redirect(url_for('index'))
    elif request.method == 'GET':
        form.otitle.data = toupdate.title
        form.oartist.data = toupdate.artist
        form.ofeature.data = toupdate.feature
        form.ocategory.data = toupdate.category
        form.oreldate.strftime = toupdate.reldate
        form.olength.data = toupdate.length

    return render_template('update.html', form=form, message=message)

@app.route('/pl')
def pl():

    #put a button on here to with a form to select all songs from a particular pl
    all_pl = Playlist.query.all()
    pl_string = ""
    for pl in all_pl:
        pl_string += "<br>" + str(pl.id) + "/" + pl.sg_title + "/" + pl.pl_name + "/" + str(pl.count) + "<br>"
    return pl_string

@app.route('/read')
def read():
    all_pl = Playlist.query.all()
    pl_string = ""
    for pl in all_pl:
        pl_string += "<br>" + str(pl.id) + "/" + pl.sg_title + "/" + pl.pl_name + "/" + str(pl.count) + "<br>"
    return pl_string

@app.route('/sing')
def sing():
    all_sg = Songs.query.all()
    sg_string = ""
    for sg in all_sg:
        sg_string += "<br>" + sg.title + "/" + sg.artist + "/" + sg.feature + "/" + sg.category + "/" + sg.reldate + "/" + sg.length + "<br>"
    return sg_string

