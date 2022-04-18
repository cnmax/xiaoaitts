from xiaoaitts.const import API
from xiaoaitts.lib.invoke import invoke


def get_device(cookies):
    data = {
        'master': 0
    }
    devices = invoke(url=API.DEVICE_LIST, data=data, cookies=cookies)
    live_devices = []
    for device in devices:
        if device['presence'] == 'online':
            live_devices.append(device)
    return live_devices
