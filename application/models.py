from application import db

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sg_num = db.Column(db.Integer, db.ForeignKey('songs.id'))
    sg_title = db.Column(db.String(30), nullable=False)
    pl_name = db.Column(db.String(30), nullable=False)
    count = db.Column(db.Integer, default=0, nullable=False)
    
class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    artist = db.Column(db.String(30), nullable=False)
    feature = db.Column(db.String(30), default="None", nullable=False)
    category = db.Column(db.String(30), nullable=False)
    reldate = db.Column('Date', db.String(30), nullable=False)
    length = db.Column(db.String(30), nullable=False)
    playlist = db.relationship('Playlist', backref='songsfk')
    
