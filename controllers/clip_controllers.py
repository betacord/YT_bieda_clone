from datetime import datetime

from flask import render_template, request, redirect, abort

from models.clip import ClipModel


def index():
    highest_rated = ClipModel.highest_rated(3)
    last_added = ClipModel.last_added(3)

    return render_template(
        'index.html',
        highest_rated=highest_rated,
        last_added=last_added,
    )


def add_clip():
    if request.method == 'POST':
        req = request.form

        new_clip = ClipModel(
            title=req['title'],
            description=req['description'],
            yt_id=req['yt_id'],
            date_added=datetime.now(),
            score=0,
        )
        new_clip.save()

        return redirect(request.url)

    return render_template('add.html')


def watch_clip(clip_id):
    if clip_details := ClipModel.find_by_id(clip_id):
        comments = clip_details.comments.all()
        return render_template('watch.html', clip=clip_details, comments=comments)

    abort(404)


def like_clip(clip_id):
    if clip := ClipModel.find_by_id(clip_id):
        clip.score += 1
        clip.save()

        return redirect(request.referrer)

    abort(404)


def unlike_clip(clip_id):
    if clip := ClipModel.find_by_id(clip_id):
        clip.score -= 1
        clip.save()

        return redirect(request.referrer)

    abort(404)
