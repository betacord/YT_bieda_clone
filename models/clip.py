# https://www.youtube.com/watch?v=LcapeUGqMhg
# https://i.ytimg.com/vi/LcapeUGqMhg/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLCbarvnzwIJh6Yjekv1jQUwcKU-iQ
# <iframe width="560" height="315" src="https://www.youtube.com/embed/LcapeUGqMhg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
from sqlalchemy import desc

from db import db


class ClipModel(db.Model):
    __tablename__ = 'clips'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    yt_id = db.Column(db.String(15))
    date_added = db.Column(db.DateTime)
    score = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, clip_id):
        return cls.query.filter_by(id=clip_id).first()

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def highest_rated(cls, n):
        return cls.query.order_by(desc(cls.score)).limit(n).all()

    @classmethod
    def top_rated(cls, n):
        return cls.query.order_by(desc(cls.date_added)).limit(n).all()
