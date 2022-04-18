from xiaoaitts.lib.invoke import ubus


def next(ticket):
    message = {
        'action': 'next',
        'media': 'app_ios'
    }
    return ubus(ticket, message=message, method='player_play_operation', path='mediaplayer')
