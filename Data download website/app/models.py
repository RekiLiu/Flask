from app import mysql


class Ins(mysql.Model):
    __tablename__ = 'ins'
    post_id = mysql.Column(mysql.String(191), primary_key=True)
    post_url = mysql.Column(mysql.String(191))
    keywords = mysql.Column(mysql.String(191))
    type = mysql.Column(mysql.String(191))
    is_ad = mysql.Column(mysql.Integer())
    is_video = mysql.Column(mysql.Integer())
    video_duration = mysql.Column(mysql.String(191))
    user_id = mysql.Column(mysql.String(191))
    user_name = mysql.Column(mysql.String(191))
    user_fullname = mysql.Column(mysql.Text)
    user_biography = mysql.Column(mysql.Text)
    user_following = mysql.Column(mysql.Integer())
    user_followed_by = mysql.Column(mysql.Integer())
    post_link = mysql.Column(mysql.String(191))
    img_description = mysql.Column(mysql.Text)
    cover_height = mysql.Column(mysql.String(191))
    cover_width = mysql.Column(mysql.String(191))
    cover_link = mysql.Column(mysql.Text)
    img_links = mysql.Column(mysql.Text)
    video_link = mysql.Column(mysql.Text)
    content = mysql.Column(mysql.Text)
    machine_translation_language = mysql.Column(mysql.String(191))
    machine_translation_content = mysql.Column(mysql.Text)
    liked_count = mysql.Column(mysql.Text)
    comment_count = mysql.Column(mysql.Integer())
    video_view_count = mysql.Column(mysql.Integer())
    pub_time = mysql.Column(mysql.String(191))
    at = mysql.Column(mysql.Text)
    hashtag = mysql.Column(mysql.Text)

    def __repr__(self):
        post_id = str(self.post_id)
        post_url = str(self.post_url)
        keywords = str(self.keywords)
        type = str(self.type)
        is_ad = str(self.is_ad)
        is_video = str(self.is_video)
        video_duration = str(self.video_duration)
        user_id = str(self.user_id)
        user_name = str(self.user_name)
        user_fullname = str(self.user_fullname)
        user_biography = str(self.user_biography)
        user_following = str(self.user_following)
        user_followed_by = str(self.user_followed_by)
        post_link = str(self.post_link)
        img_description = str(self.img_description)
        cover_height = str(self.cover_height)
        cover_width = str(self.cover_width)
        cover_link = str(self.cover_link)
        img_links = str(self.img_links)
        video_link = str(self.video_link)
        content = str(self.content)
        machine_translation_language = str(self.machine_translation_language)
        machine_translation_content = str(self.machine_translation_content)
        liked_count = str(self.liked_count)
        comment_count = str(self.comment_count)
        video_view_count = str(self.video_view_count)
        pub_time = str(self.pub_time)
        at = str(self.at)
        hashtag = str(self.hashtag)

        return '<%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s>' % (
            post_id, post_url, keywords, type, is_ad, is_video, video_duration, user_id, user_name, user_fullname,
            user_biography,
            user_following, user_followed_by, post_link, img_description, cover_height, cover_width, cover_link,
            img_links,
            video_link, content, machine_translation_language, machine_translation_content, liked_count, comment_count,
            video_view_count, pub_time, at, hashtag)


class Sticker(mysql.Model):
    __tablename__ = 'sticker'
    category_id = mysql.Column(mysql.Integer())
    sticker_id = mysql.Column(mysql.Integer(), primary_key=True)
    category_name = mysql.Column(mysql.String(191))
    sticker_name = mysql.Column(mysql.String(191))
    sticker_thumbnail = mysql.Column(mysql.String(191))

    def __repr__(self):
        category_id = str(self.category_id)
        sticker_id = str(self.sticker_id)
        category_name = str(self.category_name)
        sticker_name = str(self.sticker_name)
        sticker_thumbnail = str(self.sticker_thumbnail)
        return '<%s %s %s %s %s>' % (category_id, sticker_id, category_name, sticker_name, sticker_thumbnail)


class Post(mysql.Model):
    __tablename__ = 'post'
    post_url = mysql.Column(mysql.String(191), primary_key=True)
    keywords = mysql.Column(mysql.String(191))
    user_url = mysql.Column(mysql.String(191))
    post_link = mysql.Column(mysql.String(191))
    img_description = mysql.Column(mysql.Text)
    cover_link = mysql.Column(mysql.Text)
    img_links = mysql.Column(mysql.Text)
    video_link = mysql.Column(mysql.Text)
    content = mysql.Column(mysql.Text)
    machine_translation_language = mysql.Column(mysql.String(191))
    machine_translation_content = mysql.Column(mysql.Text)
    liked = mysql.Column(mysql.Text)
    pub_time = mysql.Column(mysql.String(191))
    at = mysql.Column(mysql.Text)
    hashtag = mysql.Column(mysql.Text)
    hashtag_url = mysql.Column(mysql.Text)

    # def __init__(self, post_url=None, keywords=None, user_url=None, post_link=None, img_description=None,
    #              cover_link=None,
    #              img_links=None, video_link=None, content=None, machine_translation_language=None,
    #              machine_translation_content=None,
    #              liked=None, pub_time=None, at=None, hashtag=None, hashtag_url=None):
    #     self.data = (post_url, keywords, user_url, post_link, img_description, cover_link,
    #                  img_links, video_link, content, machine_translation_language, machine_translation_content,
    #                  liked, pub_time, at, hashtag, hashtag_url)

    def __repr__(self):
        post_url = str(self.post_url)
        keywords = str(self.keywords)
        user_url = str(self.user_url)
        post_link = str(self.post_link)
        img_description = str(self.img_description)
        cover_link = str(self.cover_link)
        img_links = str(self.img_links)
        video_link = str(self.video_link)
        content = str(self.content)
        machine_translation_language = str(self.machine_translation_language)
        machine_translation_content = str(self.machine_translation_content)
        liked = str(self.liked)
        pub_time = str(self.pub_time)
        at = str(self.at)
        hashtag = str(self.hashtag)
        hashtag_url = str(self.hashtag_url)

        return '<%s %s %s %s %s %s %s %s ' \
               '%s %s %s %s %s %s %s %s>' % (post_url, keywords, user_url, post_link, img_description,
                                             cover_link, img_links, video_link, content,
                                             machine_translation_language, machine_translation_content,
                                             liked, pub_time, at, hashtag, hashtag_url)


class User(mysql.Model):
    __tablename__ = 'user'
    user_url = mysql.Column(mysql.String(191), primary_key=True)
    user_link = mysql.Column(mysql.String(191))
    user_name = mysql.Column(mysql.String(191))
    post_num = mysql.Column(mysql.String(191))
    followers = mysql.Column(mysql.String(191))
    following = mysql.Column(mysql.String(191))
    real_information = mysql.Column(mysql.String(191))
    description = mysql.Column(mysql.String(191))

    def __repr__(self):
        user_url = str(self.user_url)
        user_link = str(self.user_link)
        user_name = str(self.user_name)
        post_num = str(self.post_num)
        followers = str(self.followers)
        following = str(self.following)
        real_information = str(self.real_information)
        description = str(self.description)

        return '<%s %s %s %s %s %s %s %s>' % (
            user_url, user_link, user_name, post_num, followers, following, real_information, description)


class Applestore(mysql.Model):
    __tablename__ = 'apple_store'
    time = mysql.Column(mysql.String(191), primary_key=True)
    app_name = mysql.Column(mysql.String(191), primary_key=True)
    rank = mysql.Column(mysql.Integer())
    total_rank = mysql.Column(mysql.Integer())
    rating = mysql.Column(mysql.Float())
    comment_count = mysql.Column(mysql.Integer())
    download_count = mysql.Column(mysql.String(191))

    def __repr__(self):
        time = str(self.time)
        app_name = str(self.app_name)
        rank = str(self.rank)
        total_rank = str(self.total_rank)
        rating = str(self.rating)
        comment_count = str(self.comment_count)
        download_count = str(self.download_count)

        return '<%s %s %s %s %s %s %s>' % (time, app_name, rank, total_rank, rating, comment_count, download_count)


class Appledetails(mysql.Model):
    __tablename__ = 'apple_details'
    app_name = mysql.Column(mysql.String(191), primary_key=True)
    apple_id = mysql.Column(mysql.String(191))
    publish_date = mysql.Column(mysql.String(191))
    last_release_date = mysql.Column(mysql.String(191))
    category = mysql.Column(mysql.String(191))
    subtitle = mysql.Column(mysql.String(191))
    company_name = mysql.Column(mysql.String(191))
    company_link = mysql.Column(mysql.Text)
    app_link = mysql.Column(mysql.Text)

    def __repr__(self):
        app_name = str(self.app_name)
        apple_id = str(self.apple_id)
        publish_date = str(self.publish_date)
        last_release_date = str(self.last_release_date)
        category = str(self.category)
        subtitle = str(self.subtitle)
        company_name = str(self.company_name)
        company_link = str(self.company_link)
        app_link = str(self.app_link)

        return '<%s %s %s %s %s %s %s %s %s>' % (
            app_name, apple_id, publish_date, last_release_date, category, subtitle, company_name, company_link,
            app_link)


class Huaweistore(mysql.Model):
    __tablename__ = 'huawei_store'
    time = mysql.Column(mysql.String(191), primary_key=True)
    app_name = mysql.Column(mysql.String(191), primary_key=True)
    rank = mysql.Column(mysql.Integer())
    rating = mysql.Column(mysql.Float())
    comment_count = mysql.Column(mysql.Integer())
    download_count = mysql.Column(mysql.String(191))

    def __repr__(self):
        time = str(self.time)
        app_name = str(self.app_name)
        rank = str(self.rank)
        rating = str(self.rating)
        comment_count = str(self.comment_count)
        download_count = str(self.download_count)

        return '<%s %s %s %s %s %s>' % (time, app_name, rank, rating, comment_count, download_count)


class Huaweidetails(mysql.Model):
    __tablename__ = 'huawei_details'
    app_name = mysql.Column(mysql.String(191), primary_key=True)
    publish_date = mysql.Column(mysql.String(191))
    category = mysql.Column(mysql.String(191))
    subtitle = mysql.Column(mysql.String(191))
    company_name = mysql.Column(mysql.String(191))
    company_link = mysql.Column(mysql.Text)
    app_link = mysql.Column(mysql.Text)

    def __repr__(self):
        app_name = str(self.app_name)
        publish_date = str(self.publish_date)
        category = str(self.category)
        subtitle = str(self.subtitle)
        company_name = str(self.company_name)
        company_link = str(self.company_link)
        app_link = str(self.app_link)

        return '<%s %s %s %s %s %s %s>' % (
            app_name, publish_date, category, subtitle, company_name, company_link, app_link)


class Douyin(mysql.Model):
    __tablename__ = 'douyin'
    aweme_id = mysql.Column(mysql.String(191), primary_key=True)
    keywords = mysql.Column(mysql.String(191))
    hashtag = mysql.Column(mysql.String(191))
    video_url = mysql.Column(mysql.String(191))
    video_link = mysql.Column(mysql.Text)
    cover_url = mysql.Column(mysql.String(191))
    cover_link = mysql.Column(mysql.Text)
    pub_time = mysql.Column(mysql.String(191))
    is_commerce = mysql.Column(mysql.Integer())

    def __repr__(self):
        aweme_id = str(self.aweme_id)
        keywords = str(self.keywords)
        hashtag = str(self.hashtag)
        video_url = str(self.video_url)
        video_link = str(self.video_link)
        cover_url = str(self.cover_url)
        cover_link = str(self.cover_link)
        pub_time = str(self.pub_time)
        is_commerce = str(self.is_commerce)

        return '<%s %s %s %s %s %s %s %s %s>' % (
            aweme_id, keywords, hashtag, video_url, video_link, cover_url, cover_link, pub_time, is_commerce)


class Xiaohongshu(mysql.Model):
    __tablename__ = 'xhs'
    id = mysql.Column(mysql.String(191), primary_key=True)
    keywords = mysql.Column(mysql.String(191))
    title = mysql.Column(mysql.String(191))
    type = mysql.Column(mysql.String(191))
    is_ads = mysql.Column(mysql.Integer())
    liked = mysql.Column(mysql.Integer())
    liked_count = mysql.Column(mysql.Integer())
    description = mysql.Column(mysql.Text)
    post_url = mysql.Column(mysql.String(191))
    img_links = mysql.Column(mysql.Text)
    img_num = mysql.Column(mysql.Integer())
    user_nickname = mysql.Column(mysql.String(191))
    user_id = mysql.Column(mysql.String(191))
    insert_time = mysql.Column(mysql.String(191))
    pub_time = mysql.Column(mysql.String(191))

    def __repr__(self):
        id = str(self.id)
        keywords = str(self.keywords)
        title = str(self.title)
        type = str(self.type)
        is_ads = str(self.is_ads)
        liked = str(self.liked)
        liked_count = str(self.liked_count)
        description = str(self.description)
        post_url = str(self.post_url)
        img_links = str(self.img_links)
        img_num = str(self.img_num)
        user_nickname = str(self.user_nickname)
        user_id = str(self.user_id)
        insert_time = str(self.insert_time)
        pubtime = str(self.pub_time)

        return '<%s %s %s %s %s %s %s %s %s %s %s %s %s %s>' % (
            id, keywords, title, is_ads, liked, liked_count, description, post_url, img_links, img_num, user_nickname,
            user_id, insert_time, pubtime)

class CommentsApple(mysql.Model):
    __tablename__ = 'comments_apple_qimai'
    id = mysql.Column(mysql.String(191), primary_key=True)
    app_name = mysql.Column(mysql.String(191))
    app_id = mysql.Column(mysql.String(191))
    version = mysql.Column(mysql.String(191))
    pub_time = mysql.Column(mysql.String(191))
    user_name = mysql.Column(mysql.String(191))
    rating = mysql.Column(mysql.String(191))
    title = mysql.Column(mysql.String(191))
    content = mysql.Column(mysql.Text)
    is_deleted = mysql.Column(mysql.String(191))


    def __repr__(self):
        id = str(self.id)
        app_name = str(self.app_name)
        app_id = str(self.app_id)
        version = str(self.version)
        pub_time = str(self.pub_time)
        user_name = str(self.user_name)
        rating = str(self.rating)
        title = str(self.title)
        content = str(self.content)
        is_deleted = str(self.is_deleted)


        return '<%s %s %s %s %s %s %s %s %s %s>' % (
            id,app_name,app_id,version,pub_time,rating,title,content,is_deleted)


class CommentsHuawei(mysql.Model):
    __tablename__ = 'comments_huawei'
    id = mysql.Column(mysql.String(191), primary_key=True)
    app_name = mysql.Column(mysql.String(191))
    version = mysql.Column(mysql.String(191))
    rating = mysql.Column(mysql.String(191))
    stars = mysql.Column(mysql.String(191))
    pub_time = mysql.Column(mysql.String(191))
    content = mysql.Column(mysql.Text)
    user_name = mysql.Column(mysql.String(191))
    vote_count = mysql.Column(mysql.String(191))
    app_id = mysql.Column(mysql.String(191), primary_key=True)

    def __repr__(self):
        id = str(self.id)
        app_name = str(self.app_name)
        version = str(self.version)
        rating = str(self.rating)
        stars = str(self.updated)
        pub_time = str(self.title)
        content = str(self.content)
        user_name = str(self.vote_sum)
        vote_count = str(self.vote_count)
        app_id = str(self.app_id)

        return '<%s %s %s %s %s %s %s %s %s %s>' % (
            id,app_name,version,rating,stars,pub_time,content,user_name,vote_count,app_id)
