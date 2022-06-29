from application import app
from application import db
from application.models import Playlist, Songs
from flask import redirect, url_for, render_template, request
from application.forms import SongForm, UpdateForm, PlayForm, FilterForm


@app.route('/db')
def dbcon():
    todo = 'Connected'
    return todo

@app.route('/')
@app.route('/home')
def home():
    
    #hyperlink to songs db or pls
    return render_template('home.html')

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


'''@app.route('/playlists')
def playlists():

    #put a button on here to with a form to select all songs from a particular pl

    all_pl = Playlist.query.all()
    pl_string = ""
    for pl in all_pl:
        pl_string += "<br>" + str(pl.id) + "/" + pl.sg_title + "/" + pl.pl_name + "/" + str(pl.count) + "<br>"
    return pl_string'''

@app.route('/playlists', methods=['GET', 'POST'])
def playlists():

    form = FilterForm()

    search = form.pl_name.data      

    '''if form.validate_on_submit():
        searched = form.pl_name.data'''
    
    all_pl = Playlist.query.all()

    pl_string = ""
    for pl in all_pl:
        pl_string += pl.pl_name
    
    if search not in pl_string:
        return "Please select from an available playlist"
    else:
        filtered_pl = Playlist.query.filter_by(pl_name=search) 
     
    return render_template('playlists.html', form=form, playlists=filtered_pl)

@app.route('/allplaylists', methods=['GET', 'POST'])
def allplaylists():

    all_pl = Playlist.query.order_by(Playlist.pl_name)

    return render_template('allplaylists.html', playlists=all_pl)

#add song to pl
@app.route('/add_pl', methods=['GET', 'POST'])
def add_pl():
    message = ""
    form = PlayForm()

    if request.method == 'POST':
        nsgtitle = form.nsg_title.data
        nplname = form.npl_name.data
        count = Playlist.query.count()
        message = f'{nsgtitle} has been added to the {nplname} playlist'

        all_sg = Songs.query.all()

        sg_string = ""
        for sg in all_sg:
            sg_string += sg.title
        #print(sg_string)
        if nsgtitle in sg_string:
            
            new_song = Playlist(sg_title=nsgtitle, pl_name=nplname)
            db.session.add(new_song)
            db.session.commit()
        else:
            return "That song is not in available for selection please add it to the songs db and try again"  

    return render_template('add_pl.html', form=form, message=message)


@app.route('/filter')
def filter():

    pl = str(Playlist.query.filter_by(pl_name='Pop Music'))

    return pl

