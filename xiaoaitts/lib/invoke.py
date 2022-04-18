import base64
import hashlib
import hmac
import json
import os
import random
import string
import time

from xiaoaitts.const import API
from xiaoaitts.lib.error import ErrorCode, XiaoAiError
from xiaoaitts.lib.request import request


def invoke(url, data=None, method='GET', **kwargs):
    resp = request(url, data=data, method=method, **kwargs)
    if resp['code'] == 0:
        return resp['result'] if 'io.mi.com' in url else resp['data']
    raise XiaoAiError(ErrorCode.INVALID_RESULT, resp)


def ubus(ticket, message, method, path):
    def gen_request_id():
        return 'app_ios_' + ''.join(random.sample(string.digits + string.ascii_letters, 30))

    data = {
        'deviceId': ticket.device_id,
        'message': json.dumps(message, ensure_ascii=False),
        'method': method,
        'path': path,
        'requestId': gen_request_id()
    }
    try:
        return invoke(url=API.USBS, data=data, method='POST', cookies=ticket.cookies)
    except XiaoAiError as e:
        resp = e.response
        if resp['code'] == 101 and resp['data']:
            device_data = json.loads(resp['data']['device_data'])
            raise XiaoAiError(ErrorCode.UBUS_ERR, device_data['msg'])


def miio(ticket, uri, data):
    def gen_nonce():
        """Time based nonce."""
        nonce = os.urandom(8) + int(time.time() / 60).to_bytes(4, 'big')
        return base64.b64encode(nonce).decode()

    def gen_signed_nonce(ssecret, nonce):
        """Nonce signed with ssecret."""
        m = hashlib.sha256()
        m.update(base64.b64decode(ssecret))
        m.update(base64.b64decode(nonce))
        return base64.b64encode(m.digest()).decode()

    def gen_signature(url, signed_nonce, nonce, data):
        """Request signature based on url, signed_nonce, nonce and data."""
        sign = '&'.join([url, signed_nonce, nonce, 'data=' + data])
        signature = hmac.new(key=base64.b64decode(signed_nonce),
                             msg=sign.encode(),
                             digestmod=hashlib.sha256).digest()
        return base64.b64encode(signature).decode()

    def sign_data(uri, data, ssecurity):
        if not isinstance(data, str):
            data = json.dumps(data)
        nonce = gen_nonce()
        signed_nonce = gen_signed_nonce(ssecurity, nonce)
        signature = gen_signature(uri, signed_nonce, nonce, data)
        return {'_nonce': nonce, 'data': data, 'signature': signature}

    def prepare_data():
        ticket.cookies['PassportDeviceId'] = ticket.device_id
        return sign_data(uri, data, ticket.ssecurity)

    headers = {'x-xiaomi-protocal-flag-cli': 'PROTOCAL-HTTP2'}
    return invoke(url=API.MIIO + uri, data=prepare_data(), method='POST', headers=headers, cookies=ticket.cookies)


def miot(ticket, cmd, params):
    data = {
        'params': params
    }
    return miio(ticket=ticket, uri='/miotspec/' + cmd, data=data)
