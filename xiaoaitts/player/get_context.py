from xiaoaitts.lib.invoke import ubus


def get_context(ticket):
    return ubus(ticket, message={}, method='player_get_context', path='mediaplayer')
