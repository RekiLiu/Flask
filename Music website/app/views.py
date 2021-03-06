# -*-coding:utf-8-*-
import sys
import importlib
importlib.reload(sys)

import datetime
from app import app
from app import db,models,functions,forms
from flask import render_template,request,url_for,redirect
from flask import make_response,send_from_directory
from sqlalchemy import func

@app.route('/test',methods=['POST','GET'])
# def test():
#     keywords = None
#     language = None
#     form = forms.PlaylistForm()
#     if form.validate_on_submit():
#         keywords = form.keywords.data
#         tags = form.language.data
#         form.keywords.data = ''
#         form.language.data = ''
#     return render_template('test.html',form = form, language = language)

@app.route('/index')
def index():
    print(datetime.datetime.now())
    playlist_num = db.session.query(func.count(models.Playlist.playlist_id)).scalar()
    music_num = db.session.query(func.count(models.Music.music_id)).scalar()
    print(datetime.datetime.now())
    music_file_num = db.session.query(func.count(models.Music.music_id)).filter(
        models.Music.download != 'None'
    ).scalar()
    print(datetime.datetime.now())
    return render_template("index.html", playlist_num = playlist_num,
                           music_num = music_num, music_file_num = music_file_num)

@app.route('/',methods=['POST','GET'])
@app.route('/all',methods=['POST','GET'])
def all():
    form = forms.PlaylistForm()
    number = form.number.data
    keywords = form.keywords.data
    language = form.language.data
    style = form.style.data
    scene = form.scene.data
    emotion = form.emotion.data
    theme = form.theme.data
    return redirect(url_for('playlist', number = number, keywords = keywords,language = language,
                            style = style, scene = scene, emotion = emotion, theme = theme))
#
# @app.route('/playlist',methods=['POST','GET'])
# def playlist():
#     form = forms.PlaylistForm()
#     number = functions.initNumber(request.args.get('number'))
#     keywords = functions.isNone(request.args.get('keywords'))
#     language = functions.updateChoices(request.args.get('language'),form,'language')
#     style = functions.updateChoices(request.args.get('style'),form,'style')
#     scene = functions.updateChoices(request.args.get('scene'),form,'scene')
#     emotion = functions.updateChoices(request.args.get('emotion'),form,'emotion')
#     theme = functions.updateChoices(request.args.get('theme'),form,'theme')
#     page = request.args.get('page', 1, type=int)
#     per_page = int(number)
#     playlists_before_pagination = models.Playlist.query.filter(
#         models.Playlist.playlist_name.like('%' + keywords + '%'),
#         models.Playlist.playlist_tag.like('%' + language + '%'),
#         models.Playlist.playlist_tag.like('%' + style + '%'),
#         models.Playlist.playlist_tag.like('%' + scene + '%'),
#         models.Playlist.playlist_tag.like('%' + emotion + '%'),
#         models.Playlist.playlist_tag.like('%' + theme + '%'))
#     pagination_original = playlists_before_pagination.paginate(page, per_page = per_page)
#     playlists = pagination_original.items
#     cat_sorted, tag_sorted = functions.countPlaylists(playlists_before_pagination)
#     if cat_sorted and tag_sorted:
#         cat_prediction = cat_sorted[0][0]
#         tag_prediction = tag_sorted[0][0]
#         prediction_before_pagination = models.Playlist.query.filter(
#             models.Playlist.playlist_tag.like('%' + tag_prediction + '%'),
#             models.Playlist.playlist_cat.like('%' + cat_prediction + '%'))
#         prediction_page = request.args.get('page1', 1, type=int)
#         pagination_prediction = prediction_before_pagination.paginate(prediction_page, per_page=per_page)
#         predictions = pagination_prediction.items
#         playlists_column = playlists_before_pagination.with_entities(models.Playlist.playlist_name)
#         img_stream = functions.wordcloudImage(playlists_column,'playlist')
#         return render_template("playlist.html",number = number, keywords = keywords,
#                                language = language, style = style, scene = scene,
#                                emotion = emotion, theme = theme,
#                                playlists = playlists, predictions = predictions,
#                                pagination_original = pagination_original,
#                                pagination_prediction = pagination_prediction,
#                                cat_sorted= cat_sorted[:10], tag_sorted = tag_sorted[:10],
#                                img_stream = img_stream, form=form)
#     else:
#         return render_template('404.html'), 404
#
# @app.route('/music/<playlist_id>',methods=['POST','GET'])
# def music(playlist_id):
#     form = forms.MusicForm()
#     number = functions.initNumber(request.args.get('number'))
#     keywords = functions.isNone(request.args.get('keywords'))
#     artist = functions.isNone(request.args.get('artist'))
#     music_page = request.args.get('page', 1, type=int)
#     per_page = int(number)
#     musics_before_pagination = models.Music.query.filter(
#         models.Music.playlist_id.like('%' + playlist_id + '%'),
#         models.Music.music_name.like('%' + keywords + '%'),
#         models.Music.album_name.like('%' + keywords + '%'),
#         models.Music.artist_name.like('%' + artist + '%'))
#     pagination_original = musics_before_pagination.paginate(music_page, per_page=per_page)
#     musics = pagination_original.items
#     recommend_list = functions.recommendPlaylist(musics_before_pagination, playlist_id)
#     prediction_before_pagination = models.Playlist.query.filter(models.Playlist.playlist_id.in_(recommend_list))
#     prediction_page = request.args.get('page1', 1, type=int)
#     pagination_prediction = prediction_before_pagination.paginate(prediction_page, per_page=per_page)
#     predictions = pagination_prediction.items
#
#     music_id_list = []
#     lyric_list = []
#
#     music_ids = musics_before_pagination.with_entities(models.Music.music_id).all()
#     for id in music_ids:
#         music_id_list.append(id[0])
#
#     lyrics = models.Lyric.query.filter(
#         models.Lyric.music_id.in_(music_id_list)).with_entities(models.Lyric.lyric).all()
#     for lyric in lyrics:
#         lyric_list.append(lyric[0])
#
#     while '' in lyric_list:
#         lyric_list.remove('')
#
#     if len(lyric_list) == 0:
#         show_img = False
#         img_stream = ''
#     else:
#         show_img = True
#         img_stream = functions.wordcloudImage(lyric_list,'lyric')
#     return render_template("music.html", number = number, keywords = keywords,
#                            artist = artist, musics = musics,
#                            pagination_original = pagination_original,
#                            predictions = predictions, pagination_prediction = pagination_prediction,
#                            img_stream = img_stream, show_img = show_img,
#                            form = form)

@app.route('/playlist',methods=['POST','GET'])
def playlist():
    form = forms.PlaylistForm()
    number = functions.initNumber(request.args.get('number'))
    keywords = functions.isNone(request.args.get('keywords'))
    language = functions.updateChoices(request.args.get('language'),form,'language')
    style = functions.updateChoices(request.args.get('style'),form,'style')
    scene = functions.updateChoices(request.args.get('scene'),form,'scene')
    emotion = functions.updateChoices(request.args.get('emotion'),form,'emotion')
    theme = functions.updateChoices(request.args.get('theme'),form,'theme')
    page = request.args.get('page', 1, type=int)
    per_page = int(number)
    playlists_before_pagination = models.Playlist.query.filter(
        models.Playlist.playlist_name.like('%' + keywords + '%'),
        models.Playlist.playlist_tag.like('%' + language + '%'),
        models.Playlist.playlist_tag.like('%' + style + '%'),
        models.Playlist.playlist_tag.like('%' + scene + '%'),
        models.Playlist.playlist_tag.like('%' + emotion + '%'),
        models.Playlist.playlist_tag.like('%' + theme + '%'))
    pagination_original = playlists_before_pagination.paginate(page, per_page = per_page)
    playlists = pagination_original.items
    cat_sorted, tag_sorted = functions.countPlaylists(playlists_before_pagination)
    if cat_sorted and tag_sorted:
        cat_prediction = cat_sorted[0][0]
        tag_prediction = tag_sorted[0][0]
        prediction_before_pagination = models.Playlist.query.filter(
            models.Playlist.playlist_tag.like('%' + tag_prediction + '%'),
            models.Playlist.playlist_cat.like('%' + cat_prediction + '%'))
        prediction_page = request.args.get('page1', 1, type=int)
        pagination_prediction = prediction_before_pagination.paginate(prediction_page, per_page=per_page)
        predictions = pagination_prediction.items
        return render_template("playlist-simple.html",number = number, keywords = keywords,
                               language = language, style = style, scene = scene,
                               emotion = emotion, theme = theme,
                               playlists = playlists, predictions = predictions,
                               pagination_original = pagination_original,
                               pagination_prediction = pagination_prediction,
                               cat_sorted= cat_sorted[:10], tag_sorted = tag_sorted[:10],form=form)
    else:
        return render_template('404.html'), 404

@app.route('/music/<playlist_id>',methods=['POST','GET'])
def music(playlist_id):
    form = forms.MusicForm()
    number = functions.initNumber(request.args.get('number'))
    keywords = functions.isNone(request.args.get('keywords'))
    artist = functions.isNone(request.args.get('artist'))
    music_page = request.args.get('page', 1, type=int)
    per_page = int(number)
    musics_before_pagination = models.Music.query.filter(
        models.Music.playlist_id.like('%' + playlist_id + '%'),
        models.Music.music_name.like('%' + keywords + '%'),
        models.Music.album_name.like('%' + keywords + '%'),
        models.Music.artist_name.like('%' + artist + '%'))
    pagination_original = musics_before_pagination.paginate(music_page, per_page=per_page)
    musics = pagination_original.items
    recommend_list = functions.recommendPlaylist(musics_before_pagination, playlist_id)
    prediction_before_pagination = models.Playlist.query.filter(models.Playlist.playlist_id.in_(recommend_list))
    prediction_page = request.args.get('page1', 1, type=int)
    pagination_prediction = prediction_before_pagination.paginate(prediction_page, per_page=per_page)
    predictions = pagination_prediction.items
    return render_template("music-simple.html", number = number, keywords = keywords,
                           artist = artist, musics = musics,
                           pagination_original = pagination_original,
                           predictions = predictions, pagination_prediction = pagination_prediction,
                           form = form)


@app.route('/lyric/<music_id>',methods=['POST','GET'])
def lyric(music_id):
    lyrics = models.Lyric.query.filter(
        models.Lyric.music_id == music_id).all()
    lyric = functions.lyricTokenize(lyrics[0].lyric)
    return render_template("lyric.html", lyric = lyric)

@app.route('/download/<music_name>',methods=['GET'])
def download_music(music_name):
    directory = "F:\\NeteaseMusicDownload"
    return send_from_directory(directory, music_name, as_attachment=True)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/analysis',methods=['POST','GET'])
def analysis():
    artist = functions.isNone(request.form.get('artist'))
    category = functions.isNone(request.form.get('category'))
    comment = functions.isNone(request.form.get('comment'))
    return redirect(url_for('results',artist = artist,category = category,comment = comment))


@app.route('/results',methods=['POST','GET'])
def results():
    artist = functions.isNone(request.args.get('artist'))
    category = functions.isNone(request.args.get('category'))
    comment = functions.isNone(request.args.get('comment'))
    artist_keywords = ''
    category_keywords = ''
    comment_keywords = ''
    cat_playlists = []
    com_playlists = []
    music_id_list = []
    lyric_list = []

    if artist:
        musics = models.Music.query.filter(
            models.Music.artist_name.like('%' + artist + '%')).with_entities(models.Music.music_id).all()
        for music in musics:
            music_id_list.append(music[0])
        lyrics = models.Lyric.query.filter(
            models.Lyric.music_id.in_(music_id_list)).with_entities(models.Lyric.lyric).all()
        for lyric in lyrics:
            lyric_list.append(lyric[0])
        artist_keywords = functions.findKeywords(lyric_list,'lyrics')

    if comment:
        playlist_id = models.Playlist.query.filter(
            models.Playlist.playlist_tag.like('%' + comment + '%')).with_entities(models.Playlist.playlist_id)
        for i in playlist_id:
            com_playlists.append(i[0])
        print(com_playlists)
        comments_column = models.Comments.query.filter(
            models.Comments.playlist_id.in_(com_playlists)).with_entities(models.Comments.comment_content)
        comment_keywords = functions.findKeywords(comments_column,'comments')

    if category:
        playlists = models.Playlist.query.filter(
            models.Playlist.playlist_tag.like('%' + category + '%'))
        for playlist in playlists:
            cat_playlists.append(playlist.playlist_id[0])
        print(cat_playlists)

        musics = models.Music.query.filter(
            models.Music.playlist_id.in_(cat_playlists)).with_entities(models.Music.music_id).all()
        for music in musics:
            music_id_list.append(music[0])
        lyrics = models.Lyric.query.filter(
            models.Lyric.music_id.in_(music_id_list)).with_entities(models.Lyric.lyric).all()
        for lyric in lyrics:
            lyric_list.append(lyric[0])
        category_keywords = functions.findKeywords(lyric_list,'lyrics')

    return render_template("analysis.html",artist = artist, artist_keywords = artist_keywords,
                           category = category,category_keywords=category_keywords,
                           comment = comment, comment_keywords=comment_keywords)