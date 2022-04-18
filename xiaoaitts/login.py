import base64
from hashlib import sha1, md5

from xiaoaitts import XiaoAiError, ErrorCode
from xiaoaitts.const import APP_DEVICE_ID, SDK_VER, API
from xiaoaitts.lib.request import request


class Ticket:

    def __init__(self, **entries):
        self.__dict__.update(entries)

    def __repr__(self):
        return str(self.__dict__)


def login(sid, user, password):
    if not user or not password:
        raise XiaoAiError(ErrorCode.INVALID_INPUT)
    sign = get_login_sign(sid)
    auth_info = service_auth(sid, sign, user, password)
    if auth_info['code'] != 0:
        raise XiaoAiError(auth_info['code'], auth_info['desc'])
    service_token = login_mi_ai(auth_info)
    session = {
        'service_token': service_token,
        'user_id': auth_info['userId'],
        'device_id': APP_DEVICE_ID,
        'ssecurity': auth_info['ssecurity'],
    }
    session['cookies'] = get_cookie(**session)
    return session


def get_cookie(user_id=None, service_token=None, device_id=None, serial_number=None, **kwargs):
    cookies = {
        'userId': str(user_id or ''),
        'serviceToken': service_token or '',
    }
    if device_id and service_token:
        cookies.update({
            'deviceId': device_id,
            'sn': serial_number,
        })
    return cookies


def get_login_sign(sid):
    data = {
        'sid': sid,
        '_json': True
    }
    info = request(url=API.SERVICE_LOGIN, data=data)
    return {'_sign': info['_sign'], 'qs': info['qs'], 'callback': info['callback']}


def service_auth(sid, sign, user, password):
    data = {
        'user': user,
        'hash': md5(password.encode()).hexdigest().upper(),
        **sign,
        'sid': sid,
        '_json': True
    }
    cookies = {
        'deviceId': APP_DEVICE_ID,
        'sdkVersion': SDK_VER,
    }
    return request(url=API.SERVICE_AUTH, method='POST', data=data, cookies=cookies)


def login_mi_ai(auth_info):
    def gen_client_sign():
        s = 'nonce={nonce}&{ssecurity}'.format_map(auth_info)
        return base64.b64encode(sha1(s.encode()).digest()).decode()

    data = {
        'clientSign': gen_client_sign()
    }
    try:
        resp = request(url=auth_info['location'], data=data, response_type='raw')
        for cookie in resp.cookies:
            if cookie.name == 'serviceToken':
                return cookie.value
    except Exception as e:
        raise XiaoAiError(e)
    return ''


def switch_session_device(session, device):
    session.update({
        'device_id': device['deviceID'],
        'serial_number': device['serialNumber'],
        'miot_did': device['miotDID'],
        'hardware': device['hardware'],
    })
    session['cookies'] = get_cookie(**session)
    return session
