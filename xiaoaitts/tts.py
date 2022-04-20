from xiaoaitts.lib.invoke import miot
from xiaoaitts.miot import get_my_device_spec


def tts(ticket, text):
    def get_service_iid():
        device_spec = get_my_device_spec(ticket)
        for service in device_spec['services']:
            if 'actions' not in service:
                continue
            for action in service['actions']:
                if 'action:play-text' in action['type']:
                    return {
                        'siid': service['iid'],
                        'aiid': action['iid']
                    }
        return {'siid': 5, 'aiid': 1}

    params = {
        'did': ticket.miot_did,
        'in': [text],
        **get_service_iid()
    }
    return miot(ticket, cmd='action', params=params)
