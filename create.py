from application import db
from application.models import Songs, Playlist

db.drop_all()
db.create_all()

sample_song = Songs(title = "Billie Jean", artist = "Micheal Jackson", feature = "Tito", category = "Pop", reldate = '2021-08-09', length = '00:03:54')

sample_song1 = Songs(title = "Thriller", artist = "Micheal Jackson", category = "Pop", reldate = '2021-08-09', length = '00:05:35')

db.session.add(sample_song)
db.session.add(sample_song1)
db.session.commit()

sample_playlist = Playlist(sg_num = 1, sg_title = 'Billie Jean', pl_name = 'Pop Music', count = 0)

#sample_playlist1 = Playlist(songsfk = Songs.query.filter_by(title='Thriller', artist='Micheal Jackson').first(), pl_name = 'Pop Music', count = 0)

db.session.add(sample_playlist)
#db.session.add(sample_playlist1)
db.session.commit()

