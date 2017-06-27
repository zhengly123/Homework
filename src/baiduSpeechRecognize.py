import base64
import urllib
import json
import wave
import urllib.parse
import urllib.request

#需要在http://yuyin.baidu.com/asr申请服务
#密钥有效期至7月5日
def get_token():
    URL = 'http://openapi.baidu.com/oauth/2.0/token'
#在http://yuyin.baidu.com/app上的“查看key”
    _params = urllib.parse.urlencode({'grant_type': 'client_credentials',
                                'client_id': 'RegHOTHuy7zX8Gghc0eSAlAt',#API Key
                                'client_secret': '5f904326530d0a96bfc59f4e71bd1189'}).encode(encoding='UTF8')#Secret Key
    _res = urllib.request.Request(URL, _params)
    _response = urllib.request.urlopen(_res)
    _data = _response.read()
    _data = json.loads(_data)
    return _data['access_token']

#TODO:目前的上传是以分单位，需要修改为实际长度
def wav_to_text(wav_file,language):
    try:
        wav_file = open(wav_file, 'rb')
    except IOError:
        print ('文件打开错误')
        return
    wav_file = wave.open(wav_file)
    n_frames = wav_file.getnframes()
    frame_rate = wav_file.getframerate()
    print(n_frames)
    print(frame_rate)
    if frame_rate not in (8000, 16000):
        print ('文件格式错误')
        return
    audio = wav_file.readframes(n_frames)
    seconds = n_frames/frame_rate+1
    minute = int(seconds/60) + 1
    for i in range(0, minute):
        sub_audio = audio[i*60*frame_rate:(i+1)*60*frame_rate]
        base_data = base64.b64encode(sub_audio).decode('UTF-8')
        print(base_data.__str__());
        data = {"format": "wav",
                "token": get_token(),
                "len": len(sub_audio),
                "rate": frame_rate,
                "speech": base_data,
                "cuid": "B8-AC-6F-2D-7A-94",
                "channel": 1,
                "lan":language}
        data = json.dumps(data).encode(encoding='UTF8')
        res = urllib.request.Request('http://vop.baidu.com/server_api',
                              data,
                              {'content-type': 'application/json'})
        response = urllib.request.urlopen(res)
        res_data = json.loads(response.read())
        print("\n",res_data,"\n")
        print(res_data['result'][0])
        return res_data['result'][0]