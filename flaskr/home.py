from flask import (
    Blueprint, flash, g, redirect, request, session, url_for
)
from flaskr.db import get_db
from flaskr.tools import get_resp_json

bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/index', methods=('GET', 'POST'))
def index():
    category = request.form.get('category')
    gameid = request.form.get('gameid')
    # db = get_db()
    error = None

    return get_resp_json(data={
        'banners': [
            {
                'pic': '',
                'url': '',
            },
            {
                'pic': '',
                'url': '',
            },
            {
                'pic': '',
                'url': '',
            },
        ],
        'games': [
            {
                'icon': '',
                'name': '',
                'gameid': '',
            },
            {
                'icon': '',
                'name': '',
                'gameid': '',
            },
            {
                'icon': '',
                'name': '',
                'gameid': '',
            },
        ],
        'match': [
            {
                'matchid': '',
                'icon': '',
                'title': '',
                'sub_title': '',
                'start_time': '1579192268',
                'live_url': '',
                'players': [
                    {'icon': '', 'name': '', 'odds': ''},
                    {'icon': '', 'name': '', 'odds': ''},
                ]
            },
            {
                'matchid': '',
                'icon': '',
                'title': '',
                'sub_title': '',
                'start_time': '1579192268',
                'live_url': '',
                'players': [
                    {'icon': '', 'name': '', 'odds': ''},
                    {'icon': '', 'name': '', 'odds': ''},
                ]
            },
            {
                'matchid': '',
                'icon': '',
                'title': '',
                'sub_title': '',
                'start_time': '1579192268',
                'live_url': '',
                'players': [
                    {'icon': '', 'name': '', 'odds': ''},
                    {'icon': '', 'name': '', 'odds': ''},
                ]
            },
        ]
    })


@bp.route('/record', methods=('GET', 'POST'))
def record():
    is_my = request.form.get('is_my')
    # db = get_db()
    error = None

    return get_resp_json()
