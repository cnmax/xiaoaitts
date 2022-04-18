from xiaoaitts.const import API
from xiaoaitts.lib.invoke import invoke


def get_playlist(ticket):
    return invoke(url=API.PLAYLIST, cookies=ticket.cookies)
