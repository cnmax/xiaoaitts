import json

import requests

from xiaoaitts.const import MINA_UA, APP_UA, MIIO_UA


class HttpError(Exception):

    def __init__(self, response) -> None:
        self.url = response.url
        self.status = response.status_code
        self.response = response.text
        self.message = '\n'.join([
            'Request Error',
            'url: %s' % self.url,
            'status: %d' % self.status,
            'response: %s' % self.response
        ])

    def __str__(self) -> str:
        return self.message


def request(url, data, method='GET', response_type='json', headers=None, cookies=None, **kwargs):
    method = method.upper()
    content_type = 'application/x-www-form-urlencoded' if 'POST' == method else 'application/json'

    _headers = {
        'Content-Type': content_type,
        'Connection': 'keep-alive',
        'User-Agent': MINA_UA if 'mina.mi.com' in url else MIIO_UA if 'io.mi.com' in url else APP_UA,
        'Accept': '*/*',
    }
    _headers.update(headers or {})

    if method == 'GET':
        resp = requests.get(url, params=data, headers=_headers, cookies=cookies, **kwargs)
    else:
        content_type = _headers['Content-Type']
        if 'application/json' in content_type:
            resp = requests.post(url, json=data, headers=_headers, cookies=cookies, **kwargs)
        else:
            resp = requests.post(url, data=data, headers=_headers, cookies=cookies, **kwargs)

    if resp and resp.status_code == 200:
        if response_type == 'raw':
            return resp
        elif response_type == 'json':
            return json.loads(resp.text.replace('&&&START&&&', ''))
        else:
            return resp.text

    raise HttpError(resp)
