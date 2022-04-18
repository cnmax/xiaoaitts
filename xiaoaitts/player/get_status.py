import json

from xiaoaitts.lib.invoke import ubus


def get_status(ticket):
    data = ubus(ticket, message={}, method='player_get_play_status', path='mediaplayer')
    return json.loads(data['info'])
