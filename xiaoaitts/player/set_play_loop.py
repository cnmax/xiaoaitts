from xiaoaitts.lib.invoke import ubus


def set_play_loop(ticket, type=1):
    """
    :param ticket:
    :param type: 0-单曲循环，1-列表循环，3-列表随机
    :return:
    """
    message = {
        'type': type,
    }
    return ubus(ticket, message=message, method='player_set_loop', path='mediaplayer')
