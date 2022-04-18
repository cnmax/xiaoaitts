from xiaoaitts.const import get_model_spec
from xiaoaitts.lib.invoke import miot


def tts(ticket, text):
    model_spec = get_model_spec(ticket.hardware)
    params = {
        'did': ticket.miot_did,
        'siid': model_spec['siid'],
        'aiid': model_spec['aiid'],
        'in': [text]
    }
    return miot(ticket, cmd='action', params=params)
