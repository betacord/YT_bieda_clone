from datetime import datetime

from flask import request, redirect, abort

from models.comment import CommentModel


def add_comment():
    if request.method == 'POST':
        req = request.form

        new_comment = CommentModel(
            author=req['author'],
            content=req['content'],
            clip_id=req['clip_id'],
            date_added=datetime.now(),
        )
        new_comment.save()

        return redirect(request.referrer)

    abort(405)


def remove_comment():
    if request.method == 'POST':
        req = request.form

        comment = CommentModel.find_by_id(req['id'])
        comment.remove()

        return redirect(request.referrer)

    abort(405)
