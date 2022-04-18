from xiaoaitts.const import API
from xiaoaitts.lib.invoke import invoke


def get_playlist_songs(ticket, list_id, count=20, offset=0):
    data = {
        'listId': list_id,
        'count': count,
        'offset': offset,
    }
    return invoke(url=API.PLAYLIST_SONGS, data=data, cookies=ticket.cookies)
