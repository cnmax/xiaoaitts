# xiaoaitts

[![PyPI](https://img.shields.io/pypi/v/xiaoaitts.svg)](https://pypi.python.org/pypi/xiaoaitts)

小爱音箱自定义文本朗读。

> 不止是 TTS

## 安装

```bash
pip install xiaoaitts
```

## 使用

```python
from xiaoaitts import XiaoAi

# 输入小米账户名，密码
client = XiaoAi('fish', '123456')
# 朗读文本
client.say('你好，我是小爱')
```

## API

### Class: XiaoAi

#### XiaoAi(user, password)

- `username` 小米账户用户名
- `password` 账户密码

使用小米账户登录小爱音箱

### instance

XiaoAi 实例对象

#### say(text)

- `text` 文本信息

朗读指定文本，返回接口调用结果

```python
client.say('你好，我是小爱')
```

#### get_device(name=None)

- `name` 设备名称(别名)
- Returns: 设备信息

获取**在线**设备列表

```python
# 获取所有在线设备
online_devices = client.get_device()
# 获取单个设备，未找到时返回 null
room_device = client.get_device('卧室小爱')
```

#### use_device(device_id)

- `device_id` 设备id

切换指定设备。`xiaomitts` 实例化后默认使用 `get_device()` 方法返回的第一个设备，可使用此方法切换为指定设备。

```python
room_device = client.get_device('卧室小爱')
# 使用“卧室小爱”
client.use_device(room_device.get('deviceID'))
client.say('你好，我是卧室的小爱')
```

#### test()

测试连通性

```python
client.test()
```

### 媒体控制

#### set_volume(volume)

- `volume` 音量值

设置音量

```python
client.set_volume(30)
```

#### get_volume()

- Returns: 音量值

获取音量

```python
volume = client.get_volume()
```

#### volume_up()

调高音量，幅度 5

#### volume_down()

调低音量，幅度 5

#### get_status()

- Returns: 状态信息

获取设备运行状态

#### play()

继续播放

#### pause()

暂停播放

#### prev()

播放上一曲

#### next()

播放下一曲

#### set_play_loop(type=1)

- `type` 0-单曲循环 1-列表循环 3-列表随机

设置循环播放

#### get_song_info(song_id)

- `song_id` 歌曲id
- Returns: 歌曲信息

查询歌曲信息

```python
song_info = client.get_song_info('7519904358300484678')
```

#### get_my_playlist(list_id=None)

- `list_id` 歌单id
- Returns:  歌曲信息

获取用户自建歌单，当指定 `list_id` 时，将返回目标歌单内的歌曲列表

```python
# 获取歌单列表
my_playlist = client.get_my_playlist()
# 获取歌单内的歌曲列表
song_list = client.get_my_playlist('337361232731772372')
```

## 参考链接

- [https://github.com/Yonsm/ZhiMi](https://github.com/Yonsm/ZhiMi)
- [https://github.com/Yonsm/MiService](https://github.com/Yonsm/MiService)
- [https://github.com/vv314/xiaoai-tts](https://github.com/vv314/xiaoai-tts)