from app import app
from models import db, Playlist, Song, PlaylistSong

db.drop_all()
db.create_all()

p1 = Playlist(
    name="Metal!",
    description="Rock On!"
)

p2 = Playlist(
    name="K-Pop",
    description="Are any of these men!?"
)

db.session.add_all([p1, p2])
db.session.commit()


s1 = Song(
    title="The Metal",
    artist="Tenacious D"
)

s2 = Song(
    title="Beyond the Realms of Death",
    artist="Judas Priest"
)

s3 = Song(
    title="After School",
    artist="Weeekly"
)

s4 = Song(
    title="Next Level",
    artist="aespa"
)

s5 = Song(
    title="FAKE LOVE",
    artist="BTS"
)

s6 = Song(
    title="Dynamite",
    artist="BTS"
)

s7 = Song(
    title="Break The Wall",
    artist="Dreamcatcher"
)

db.session.add_all([s1, s2, s3, s4, s5, s6, s7])
db.session.commit()


ps1 = PlaylistSong(
    playlist_id = 1,
    song_id = 1
)

ps2 = PlaylistSong(
    playlist_id = 1,
    song_id = 2
)

ps3 = PlaylistSong(
    playlist_id = 1,
    song_id = 7
)

ps4 = PlaylistSong(
    playlist_id = 2,
    song_id = 3
)

ps5 = PlaylistSong(
    playlist_id = 2,
    song_id = 4
)

ps6 = PlaylistSong(
    playlist_id = 2,
    song_id = 5
)

ps7 = PlaylistSong(
    playlist_id = 2,
    song_id = 6
)

ps8 = PlaylistSong(
    playlist_id = 2,
    song_id = 7
)

db.session.add_all([ps1, ps2, ps3, ps4, ps5, ps6, ps7, ps8])
db.session.commit()