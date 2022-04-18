import json

from xiaoaitts.lib.invoke import ubus


def nlp(ticket):
    data = ubus(ticket, message={}, method='nlp_result_get', path='mibrain')
    info = json.loads(data['info'])
    return json.loads(info['result'][0]['nlp'])
