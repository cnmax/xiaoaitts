from xiaoaitts.lib.invoke import miio


def get_device(ticket, name=None, virtual_model=False, huami_devices=0):
    data = {
        'getVirtualModel': bool(virtual_model),
        'getHuamiDevices': int(huami_devices)
    }
    devices = miio(ticket, uri='/home/device_list', data=data)['list']
    return [device for device in devices if not name or name in device['name']]
