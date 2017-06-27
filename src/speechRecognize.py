import voiceRecord
import baiduSpeechRecognize

#语音识别函数，返回识别文本
#language为"en"是英文识别，"zh"是中文识别
#time是录音时长
def recordAndRecognize(language,time=5):
    WAVE_FILENAME="output.wav"
    voiceRecord.record(WAVE_FILENAME,time)
    print('Start recognizing')
    return baiduSpeechRecognize.wav_to_text(WAVE_FILENAME,language)

#Test
#recordAndRecognize("en")
#recordAndRecognize("zh",3)