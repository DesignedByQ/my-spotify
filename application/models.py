from application import db

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    count = db.Column(db.Integer, default=0, nullable=False)
    songs = db.relationship('Songs', backref='playlistfk')

class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    artist = db.Column(db.String(30), nullable=False)
    feature = db.Column(db.String(30), default="None", nullable=True)
    category = db.Column(db.String(30), nullable=False)
    reldate = db.Column('Date', db.String(30), nullable=False)
    length = db.Column(db.String(30), nullable=False)
    playlist_title = db.Column(db.String, db.ForeignKey('playlist.title'), nullable=False)
    
'''class Albums(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    artist = db.Column(db.String(30), nullable=False)
    category = db.Column(db.String(30), nullable=False)
    reldate = db.Column('Date', db.String(30), nullable=False)
    totallen = db.Column(db.String(30), nullable=False)
    album = db.Column(db.Integer, nullable=False)

class Playlists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), default="New Playlist")
    count = db.Column(db.Integer, default=0 nullable=False)
    
class PlaylistSongs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    artist = db.Column(db.String(30), nullable=False)
    reldate = db.Column('Date', db.String(30), nullable=False)
    playlist_id = db.Column(db.Integer, nullable=False)
    songs_id = db.Column(db.Integer, nullable=False)

class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    artist = db.Column(db.String(30), nullable=False)
    feature = db.Column(db.String(30))
    category = db.Column(db.String(30), nullable=False)
    reldate = db.Column('Date', db.String(30), nullable=False)
    length = db.Column(db.String(30), nullable=False)
    album_id = db.Column(db.Integer, nullable=False)'''