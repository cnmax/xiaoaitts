from xiaoaitts import XiaoAiError, ErrorCode
from xiaoaitts.miot.get_device import get_device
from xiaoaitts.miot.get_device_spec import get_device_spec


def get_my_device_spec(ticket):
    def get_current_device():
        devices = get_device(ticket)
        for device in devices:
            if device['did'] == ticket.miot_did:
                return device
        raise XiaoAiError(ErrorCode.NO_DEVICE, ticket.miot_did)

    current_device = get_current_device()
    miot_specs = get_device_spec()
    for model, _type in miot_specs.items():
        if model == current_device['model']:
            return get_device_spec(_type)
    raise XiaoAiError(ErrorCode.NO_DEVICE, ticket.miot_did)
