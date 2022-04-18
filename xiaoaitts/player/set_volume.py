from xiaoaitts.lib.invoke import ubus


def set_volume(ticket, volume):
    volume = min(max(volume, 0), 100)
    message = {
        'volume': volume,
    }
    return ubus(ticket, message=message, method='player_set_volume', path='mediaplayer')
