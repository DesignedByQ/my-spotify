from application import db
from application.models import Songs, Playlist

db.drop_all()
db.create_all()

sample_playlist = Playlist(title = 'pop music', count = 0)

db.session.add(sample_playlist)
db.session.commit()

sample_song = Songs(title = "billie jean", artist = "Micheal Jackson", feature = "tito", category = "pop", reldate = '2021-08-09', length = '00:03:54', playlistfk = sample_playlist)

sample_song1 = Songs(title = "thriller", artist = "Micheal Jackson", category = "pop", reldate = '2021-08-09', length = '00:05:35', playlistfk = Playlist.query.filter_by(title='pop music').first())

db.session.add(sample_song1)
db.session.commit()