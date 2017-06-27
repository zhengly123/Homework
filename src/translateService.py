# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import json

class TranslateService:

    #auto translation
    def translate(self,content):
        #print('hello world' + content)
        Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
        #创建Form_Data字典，存储上图的Form Data
        Form_Data = {}
        Form_Data['action'] = 'FY_BY_CLICKBUTTON'
        Form_Data['client'] = 'fanyideskweb'
        Form_Data['doctype'] = 'json'
        Form_Data['from'] = 'AUTO'
        Form_Data['to'] = 'AUTO'
        Form_Data['i'] = content
        Form_Data['keyfrom'] = 'fanyi.web'
        Form_Data['smartresult'] = 'dict'
        Form_Data['typoResult'] = 'true'
        Form_Data['version'] = '2.1'
        #使用urlencode方法转换标准格式
        data = parse.urlencode(Form_Data).encode('utf-8')
        #传递Request对象和转换完格式的数据
        response = request.urlopen(Request_URL,data)
        #读取信息并解码
        html = response.read().decode('utf-8')
        #使用JSON
        translate_results = json.loads(html)
        #找到翻译结果
        translate_result = translate_results['translateResult'][0][0]['tgt']

        #smart = translate_results['smartResult']['entries']
        return translate_result
