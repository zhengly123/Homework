import voiceRecord
import baiduSpeechRecognize
import threading

class SpeechRecognize(threading.Thread):

    #语音识别函数，返回识别文本
    #language为"en"是英文识别，"zh"是中文识别
    #time是录音时长
    def recordAndRecognize(self,language,callbackSpeech,time=5):
        t = threading.Thread(target=self.worker,args=(language,callbackSpeech,time))
        t.start()


    def worker(self,language,callbackSpeech,time=5):
        WAVE_FILENAME="output.wav"
        voiceRecord.record(WAVE_FILENAME,time)
        print('Start recognizing')
        result = baiduSpeechRecognize.wav_to_text(WAVE_FILENAME,language)
        callbackSpeech(language,result)

#Test
#recordAndRecognize("en")
#recordAndRecognize("zh",3)