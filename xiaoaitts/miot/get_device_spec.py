import json
import os
from functools import lru_cache

from xiaoaitts.lib.request import request

"""
http://miot-spec.org/miot-spec-v2/instances?status=all
https://miot-spec.org/miot-spec-v2/instance?type=urn:miot-spec-v2:device:speaker:0000A015:xiaomi-x08c:1
"""


@lru_cache(maxsize=None)
def get_device_spec(type=None):
    if not type or not type.startswith('urn'):
        def get_spec(all):
            if not type:
                return all
            ret = {}
            for m, t in all.items():
                if type == m:
                    return {m: t}
                elif type in m:
                    ret[m] = t
            return ret

        import tempfile
        path = os.path.join(tempfile.gettempdir(), 'xiaoaitts_miot_specs.json')
        try:
            with open(path) as f:
                result = get_spec(json.load(f))
        except:
            result = None
        if not result:
            resp = request('http://miot-spec.org/miot-spec-v2/instances?status=all', data={})
            all = {i['model']: i['type'] for i in resp['instances']}
            with open(path, 'w') as f:
                json.dump(all, f)
            result = get_spec(all)
        if len(result) != 1:
            return result
        type = list(result.values())[0]

    return request('http://miot-spec.org/miot-spec-v2/instance?type=' + type, data={})
