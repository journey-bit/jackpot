from flask import current_app


def get_resp_json(ec=200, em='OK', data={}):
    return {
        'ec': ec,
        'em': em,
        'data': data
    }
