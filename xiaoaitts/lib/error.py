import json

from xiaoaitts.lib.request import HttpError


class ErrorCode:
    AURH_ERR = 401,
    INVALID_INPUT = 1,
    NO_DEVICE = 2,
    UBUS_ERR = 3,
    INVALID_RESULT = 4


ERROR_CODE_MAP = {
    ErrorCode.AURH_ERR: 'Session 校验失败，请重新登录',
    ErrorCode.NO_DEVICE: '未找到在线设备，请检查设备连接',
    ErrorCode.INVALID_INPUT: '参数不合法，请查阅文档',
    ErrorCode.INVALID_RESULT: '接口错误',
    ErrorCode.UBUS_ERR: '请检查设备连接'
}


class XiaoAiError(Exception):

    def __init__(self, code, error_message='') -> None:
        if isinstance(code, HttpError):
            if code.status in ERROR_CODE_MAP:
                message = ERROR_CODE_MAP[code.status]
            else:
                message = '网络请求错误'
                error_message = code.message
        elif code == ErrorCode.INVALID_RESULT:
            self.response = error_message
            message = ERROR_CODE_MAP[code]
        else:
            message = ERROR_CODE_MAP.get(code, '')

        if not isinstance(error_message, str):
            error_message = json.dumps(error_message)
        self.message = error_message + (' - ' + message if message else '')

    def __str__(self) -> str:
        return self.message
