from xiaoaitts.player.get_context import get_context
from xiaoaitts.player.get_playlist import get_playlist
from xiaoaitts.player.get_playlist_songs import get_playlist_songs
from xiaoaitts.player.get_song_info import get_song_info
from xiaoaitts.player.get_status import get_status
from xiaoaitts.player.get_volume import get_volume
from xiaoaitts.player.next import next
from xiaoaitts.player.pause import pause
from xiaoaitts.player.play import play
from xiaoaitts.player.play_album_playlist import play_album_playlist
from xiaoaitts.player.play_url import play_url
from xiaoaitts.player.prev import prev
from xiaoaitts.player.set_play_loop import set_play_loop
from xiaoaitts.player.set_volume import set_volume
from xiaoaitts.player.toggle_play_state import toggle_play_state

VOLUME_STEP = 5


def volume_up(ticket):
    volume = get_volume(ticket)
    return set_volume(ticket, volume + VOLUME_STEP)


def volume_down(ticket):
    volume = get_volume(ticket)
    return set_volume(ticket, volume - VOLUME_STEP)


def get_my_playlist(ticket, list_id=None):
    playlist = get_playlist(ticket)
    if not list_id:
        return playlist
    song_list = None
    for item in playlist:
        if item['id'] == int(list_id):
            song_list = item
            break
    show_count = song_list['songCount'] if song_list else 0
    return get_playlist_songs(ticket, list_id=list_id, count=show_count)
