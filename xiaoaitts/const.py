APP_DEVICE_ID = '3C861A5820190429'
SDK_VER = '3.9'
APP_UA = 'APP/com.xiaomi.mihome APPV/6.0.103 iosPassportSDK/3.9.0 iOS/14.4 miHSTS'
MINA_UA = 'MiHome/6.0.103 (com.xiaomi.mihome; build:6.0.103.1; iOS 14.4.0) Alamofire/6.0.103 MICO/iOSApp/appStore/6.0.103'
MIIO_UA = 'iOS-14.4-6.0.103-iPhone12,3--D7744744F7AF32F0544445285880DD63E47D9BE9-8816080-84A3F44E137B71AE-iPhone'

MODEL_SPECS = {
    # 已验证：lx01=小爱迷你音箱，lx5a=小爱音箱Play，lx04=小爱触屏音箱，x08c=红米小爱音箱
    # 未测试：l04m，l04n，l05c，l06a，lx05，lx06，s12，x08a
    'lx04,l04m,x08a': {'execute_aiid': 4},
    'l04n,l05c': {'aiid': 3, 'execute_aiid': 4},
    'x08c': {'siid': 3, 'execute_siid': 3, 'volume_siid': 4},

    # TODO: '123': {'aiid': 3, 'execute_aiid': 4}, # 未知型号，直接执行文本参数只有一个，应该不能工作，需要调整代码，但可能市面上不存在这个型号，先忽略
    # TODO：'v1,v3': # 不支持 MIoT TTS，需要引入 MiNA Service 支持，我手上没有相关设备，如果有人需要可以提出
}


def get_model_spec(model):
    default = {
        'siid': 5,
        'aiid': 1,
        'execute_siid': 5,
        'execute_aiid': 5,
        'volume_siid': 2,
        'volume_piid': 1
    }
    if model:
        model = model.lower().split('.')[-1]
        for k in MODEL_SPECS:
            if model in k:
                default.update(MODEL_SPECS[k])
    return default


class API:
    MIIO = 'https://api.io.mi.com/app'
    USBS = 'https://api2.mina.mi.com/remote/ubus'
    SERVICE_AUTH = 'https://account.xiaomi.com/pass/serviceLoginAuth2'
    SERVICE_LOGIN = 'https://account.xiaomi.com/pass/serviceLogin'
    PLAYLIST = 'https://api2.mina.mi.com/music/playlist/v2/lists'
    PLAYLIST_SONGS = 'https://api2.mina.mi.com/music/playlist/v2/songs'
    SONG_INFO = 'https://api2.mina.mi.com/music/song_info'
    DEVICE_LIST = 'https://api2.mina.mi.com/admin/v2/device_list'
