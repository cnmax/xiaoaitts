from xiaoaitts.lib.invoke import ubus


def play(ticket):
    message = {
        'action': 'play',
        'media': 'app_ios'
    }
    return ubus(ticket, message=message, method='player_play_operation', path='mediaplayer')
