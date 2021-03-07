
from flask import Blueprint, request

from . import mine

bp = Blueprint('kipi', __name__, url_prefix='/kipi')

@bp.route('/kill', methods=('POST',))
def kill():
    if request.method == 'POST':
        mine.MinecraftProcess.kill_server()
    return 

@bp.route('/start', methods=('POST',))
def start():
    if request.method == 'POST':
        mine.MinecraftProcess.start_server()
    return

@bp.route('/restart', methods=('POST',))
def restart():
    if request.method == 'POST':
        mine.MinecraftProcess.restart_server()
    return
