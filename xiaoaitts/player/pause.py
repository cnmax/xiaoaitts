from xiaoaitts.lib.invoke import ubus


def pause(ticket):
    message = {
        'action': 'pause',
        'media': 'app_ios'
    }
    return ubus(ticket, message=message, method='player_play_operation', path='mediaplayer')
