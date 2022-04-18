from xiaoaitts.lib.invoke import ubus


def play_album_playlist(ticket, album_playlist_id, type=1, start_offset=1):
    message = {
        'type': type,
        'id': album_playlist_id,
        'startOffset': start_offset,
        'media': 'common'
    }
    return ubus(ticket, message=message, method='player_play_album_playlist', path='mediaplayer')
