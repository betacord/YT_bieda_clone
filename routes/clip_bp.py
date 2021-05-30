from flask import Blueprint

from controllers.clip_controllers import index, add_clip, watch_clip, like_clip, unlike_clip

clip_bp = Blueprint('clip_bp', __name__)

clip_bp.route('/', methods=['GET'])(index)
clip_bp.route('/add', methods=['GET', 'POST'])(add_clip)
clip_bp.route('/clip/<clip_id>')(watch_clip)
clip_bp.route('/like_clip/<clip_id>', methods=['GET'])(like_clip)
clip_bp.route('/unlike_clip/<clip_id>', methods=['GET'])(unlike_clip)
