from flask import Blueprint

from controllers.comment_controllers import add_comment, remove_comment

comment_bp = Blueprint('comment_bp', __name__)

comment_bp.route('/add', methods=['POST'])(add_comment)
comment_bp.route('/remove', methods=['POST'])(remove_comment)
