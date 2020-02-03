from flask import (
    Blueprint, flash, g, redirect, request, session, url_for
)
from flaskr.db import get_db
from flaskr.tools import get_resp_json

bp = Blueprint('bet', __name__, url_prefix='/bet')


@bp.route('/rules', methods=('GET', 'POST'))
def rules():
    matchid = request.form.get('matchid')
    # db = get_db()
    error = None
    return get_resp_json(data={
        'icon': '',
        'title': '',
        'sub_title': '',
        'start_time': '1579192268',
        'players': [
            {'icon': '', 'name': ''},
            {'icon': '', 'name': ''},
        ],
        'rules': [
            {
                'text': '',
                'rules': [
                    {'ruleid': '', 'desc': '', 'odds': ''},
                    {'ruleid': '', 'desc': '', 'odds': ''}
                ]
            },
            {
                'text': '',
                'rules': [
                    {'ruleid': '', 'desc': '', 'odds': ''},
                    {'ruleid': '', 'desc': '', 'odds': ''}
                ]
            }
        ]
    })

@bp.route('/bet', methods=('GET', 'POST'))
def bet():
    matchid = request.form.get('matchid')
    ruleid = request.form.get('ruleid')
    amount = request.form.get('amount')

    # db = get_db()
    error = None
    return get_resp_json()
