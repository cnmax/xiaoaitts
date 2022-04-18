from xiaoaitts.lib.invoke import ubus


def prev(ticket):
    message = {
        'action': 'prev',
        'media': 'app_ios'
    }
    return ubus(ticket, message=message, method='player_play_operation', path='mediaplayer')
