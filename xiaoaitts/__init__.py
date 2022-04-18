from xiaoaitts import player
from xiaoaitts.get_device import get_device
from xiaoaitts.lib.error import XiaoAiError, ErrorCode
from xiaoaitts.lib.invoke import ubus
from xiaoaitts.login import login, switch_session_device, Ticket
from xiaoaitts.tts import tts


class XiaoAi:

    def __init__(self, user, password):
        self.current_device = None
        self.mina_session = login('micoapi', user, password)
        devices = get_device(self.mina_session['cookies'])
        if len(devices) == 0:
            return
        self.current_device = devices[0]
        self.mina_session = switch_session_device(self.mina_session, self.current_device)

        self.miio_session = login('xiaomiio', user, password)
        self.miio_session = switch_session_device(self.miio_session, self.current_device)

    def test(self):
        return ubus(Ticket(**self.mina_session),
                    message={'vendor_name': 'XiaoMi_M88'},
                    method='tts_vendor_switch',
                    path='mibrain')

    def get_device(self, name=None):
        devices = get_device(self.mina_session['cookies'])
        if not name:
            return devices
        target = []
        for device in devices:
            if name in device['name']:
                target.append(device)
        return target or None

    def use_device(self, device_id):
        session = self.mina_session
        devices = get_device(session['cookies'])
        device = None
        for _device in devices:
            if _device['deviceID'] == device_id:
                device = _device
                break
        if not device:
            raise XiaoAiError(ErrorCode.NO_DEVICE, device_id)
        self.current_device = device
        self.mina_session = switch_session_device(session, device)
        self.miio_session = switch_session_device(self.miio_session, device)

    def _call(self, method, **kwargs):
        if method.__name__ == 'tts':
            ticket = Ticket(**self.miio_session)
        else:
            ticket = Ticket(**self.mina_session)
        return method(ticket, **kwargs)

    def say(self, text):
        return self._call(tts, text=text)

    def set_volume(self, volume):
        if isinstance(volume, int):
            raise XiaoAiError(ErrorCode.INVALID_INPUT)
        return self._call(player.set_volume, volume=volume)

    def get_volume(self):
        return self._call(player.get_volume)

    def volume_up(self):
        return self._call(player.volume_up)

    def volume_down(self):
        return self._call(player.volume_down)

    def play(self):
        return self._call(player.play)

    def pause(self):
        return self._call(player.pause)

    def prev(self):
        return self._call(player.prev)

    def next(self):
        return self._call(player.next)

    def set_play_loop(self, type=1):
        return self._call(player.set_play_loop, type=type)

    def get_status(self):
        return self._call(player.get_status)

    def get_song_info(self, song_id):
        return self._call(player.get_song_info, song_id=song_id)

    def get_my_playlist(self, list_id=None):
        return self._call(player.get_my_playlist, list_id=list_id)
