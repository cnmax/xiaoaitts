from xiaoaitts.lib.invoke import ubus


def toggle_play_state(ticket):
    message = {
        'action': 'toggle',
    }
    return ubus(ticket, message=message, method='player_play_operation', path='mediaplayer')
