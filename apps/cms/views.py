from flask import Blueprint

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/hello')
def index():
    return "123456"