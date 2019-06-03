# -*-coding:utf-8-*-

from app import db

class Category(db.Model):
    __tablename__ = 'categorylist'
    category_name = db.Column(db.String(255),primary_key=True)
    category_url = db.Column(db.String(255))

    def __repr__(self):
        category_name = str(self.category_name)
        category_url = str(self.category_url)

        return '<%s %s >' % (category_name,category_url)

class Playlist(db.Model):
    __tablename__ = 'playlist'
    playlist_id = db.Column(db.String(255),primary_key=True)
    playlist_url = db.Column(db.String(255))
    playlist_name = db.Column(db.String(255))
    playlist_cat = db.Column(db.String(255))
    playlist_tag = db.Column(db.String(255))
    playlist_author = db.Column(db.String(255))
    playlist_author_url = db.Column(db.String(255))
    playlist_pubtime = db.Column(db.String(255))
    playlist_songnum = db.Column(db.String(255))
    playlist_desc = db.Column(db.String(255))
    playlist_fav_count = db.Column(db.String(255))
    playlist_share_count = db.Column(db.String(255))
    playlist_comment_count = db.Column(db.String(255))

    def __repr__(self):
        playlist_id = str(self.playlist_id)
        playlist_url = str(self.playlist_url)
        playlist_name = str(self.playlist_name)
        playlist_cat = str(self.playlist_cat)
        playlist_tag = str(self.playlist_tag)
        playlist_author = str(self.playlist_author)
        playlist_author_url = str(self.playlist_author_url)
        playlist_pubtime = str(self.playlist_pubtime)
        playlist_songnum = str(self.playlist_songnum)
        playlist_desc = str(self.playlist_desc)
        playlist_fav_count = str(self.playlist_fav_count)
        playlist_share_count = str(self.playlist_share_count)
        playlist_comment_count = str(self.playlist_comment_count)

        return '<%s %s %s %s %s %s %s ' \
               '%s %s %s %s %s %s>' % (playlist_id,playlist_url,playlist_name,
                                       playlist_cat,playlist_tag,playlist_author,
                                       playlist_author_url,playlist_pubtime,playlist_songnum,
                                       playlist_desc,playlist_fav_count,
                                       playlist_share_count,playlist_comment_count)

class Music(db.Model):
    __tablename__ = 'music'
    music_id = db.Column(db.String(255),primary_key=True)
    playlist_id = db.Column(db.String(255))
    music_name = db.Column(db.String(255))
    music_url = db.Column(db.String(255))
    artist_name = db.Column(db.String(255))
    artist_url = db.Column(db.String(255))
    album_name = db.Column(db.String(255))
    album_url = db.Column(db.String(255))
    lyric = db.Column(db.Text)
    download = db.Column(db.String(255))

    def __repr__(self):
        music_id = str(self.music_id)
        playlist_id = str(self.playlist_id)
        music_name = str(self.music_name)
        music_url = str(self.music_url)
        artist_name = str(self.artist_name)
        artist_url = str(self.artist_url)
        album_name = str(self.album_name)
        album_url = str(self.album_url)
        lyric = str(self.lyric)
        download = str(self.download)

        return '<%s %s %s %s %s ' \
               '%s %s %s %s %s >' % (music_id, playlist_id,music_name,
                                     music_url, artist_name, artist_url,
                                     album_name, album_url, lyric, download)

class PlaylistBGM(db.Model):
    __tablename__ = 'playlist_bgm'
    playlist_id = db.Column(db.String(255),primary_key=True)
    playlist_url = db.Column(db.String(255))
    playlist_name = db.Column(db.String(255))
    playlist_cat = db.Column(db.String(255))
    playlist_tag = db.Column(db.String(255))
    playlist_author = db.Column(db.String(255))
    playlist_author_url = db.Column(db.String(255))
    playlist_pubtime = db.Column(db.String(255))
    playlist_songnum = db.Column(db.String(255))
    playlist_desc = db.Column(db.String(255))
    playlist_fav_count = db.Column(db.String(255))
    playlist_share_count = db.Column(db.String(255))
    playlist_comment_count = db.Column(db.String(255))

    def __repr__(self):
        playlist_id = str(self.playlist_id)
        playlist_url = str(self.playlist_url)
        playlist_name = str(self.playlist_name)
        playlist_cat = str(self.playlist_cat)
        playlist_tag = str(self.playlist_tag)
        playlist_author = str(self.playlist_author)
        playlist_author_url = str(self.playlist_author_url)
        playlist_pubtime = str(self.playlist_pubtime)
        playlist_songnum = str(self.playlist_songnum)
        playlist_desc = str(self.playlist_desc)
        playlist_fav_count = str(self.playlist_fav_count)
        playlist_share_count = str(self.playlist_share_count)
        playlist_comment_count = str(self.playlist_comment_count)

        return '<%s %s %s %s %s %s %s ' \
               '%s %s %s %s %s %s>' % (playlist_id,playlist_url,playlist_name,
                                       playlist_cat,playlist_tag,playlist_author,
                                       playlist_author_url,playlist_pubtime,playlist_songnum,
                                       playlist_desc,playlist_fav_count,
                                       playlist_share_count,playlist_comment_count)

class MusicBGM(db.Model):
    __tablename__ = 'music_bgm'
    music_id = db.Column(db.String(255),primary_key=True)
    playlist_id = db.Column(db.String(255))
    music_name = db.Column(db.String(255))
    music_url = db.Column(db.String(255))
    artist_name = db.Column(db.String(255))
    artist_url = db.Column(db.String(255))
    album_name = db.Column(db.String(255))
    album_url = db.Column(db.String(255))
    lyric = db.Column(db.Text)
    download = db.Column(db.String(255))

    def __repr__(self):
        music_id = str(self.music_id)
        playlist_id = str(self.playlist_id)
        music_name = str(self.music_name)
        music_url = str(self.music_url)
        artist_name = str(self.artist_name)
        artist_url = str(self.artist_url)
        album_name = str(self.album_name)
        album_url = str(self.album_url)
        lyric = str(self.lyric)
        download = str(self.download)

        return '<%s %s %s %s %s ' \
               '%s %s %s %s %s >' % (music_id, playlist_id,music_name,
                                     music_url, artist_name, artist_url,
                                     album_name, album_url, lyric, download)



