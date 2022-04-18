from xiaoaitts.player import get_status


def get_volume(ticket):
    return get_status(ticket)['volume']
