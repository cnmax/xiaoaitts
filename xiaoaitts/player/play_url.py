from xiaoaitts.lib.invoke import ubus


def play_url(ticket, url, type=1):
    message = {
        'type': type,
        'url': url,
        'media': 'app_ios'
    }
    return ubus(ticket, message=message, method='player_play_url', path='mediaplayer')
