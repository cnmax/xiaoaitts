from xiaoaitts.const import API
from xiaoaitts.lib.invoke import invoke


def get_song_info(ticket, song_id):
    data = {
        'songId': song_id
    }
    return invoke(url=API.SONG_INFO, data=data, cookies=ticket.cookies)
