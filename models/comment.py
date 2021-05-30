from db import db


class CommentModel(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(80))
    content = db.Column(db.String)
    date_added = db.Column(db.DateTime)

    clip_id = db.Column(db.Integer, db.ForeignKey('clips.id'), nullable=False)
    clip = db.relationship('ClipModel')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, comment_id):
        return cls.query.filter_by(id=comment_id).first()
