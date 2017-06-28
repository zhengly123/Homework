# -*- coding: UTF-8 -*-
from tkinter import *
import tkinter.messagebox
from translateService import *
from speechRecognize import *
class Application:

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 300
    TITLE = "Online Translation"

    def __init__(self):
        self.frame = Tk()
        self.__service = TranslateService()
        self.__speech = SpeechRecognize()
        self.frame.title(Application.TITLE)
        self.frame.maxsize(Application.WINDOW_WIDTH, Application.WINDOW_HEIGHT)
        self.frame.minsize(Application.WINDOW_WIDTH, Application.WINDOW_HEIGHT)
        self.center_window(self.frame, 700, 340)
        self.createSourceText()
        self.createTargetText()
        self.createButton()
        self.frame.mainloop()

    def center_window(self,root, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
        root.geometry(size)

    def createSourceText(self):
        self.text_source = Text(self.frame,height = "16",width = 40)
        self.text_source.grid(row = 1,column = 1,columnspan=3,rowspan =2,padx=10,pady=10)

    def createTargetText(self):
        self.text_target = Text(self.frame,height = "16",width = 40)
        self.text_target.grid(row = 1,column = 8,columnspan=3,rowspan =1,padx=10,pady=0)
        #self.text_target.configure(state="disabled")

    def createButton(self):
        self.button_say_chinese = Button(self.frame,text = "say chinese",width = 10)
        self.button_say_english = Button(self.frame,text = "say english",width = 10)
        self.button_translate = Button(self.frame,text = "auto translation",width = 20)
        self.button_clear = Button(self.frame,text = "clear",width = 10)

        self.var1 = IntVar()
        self.button_check = Checkbutton(self.frame,variable = self.var1,text = "auto translation",width = 20)
        self.button_check.select()
        self.button_say_chinese.grid(row = 0,column = 1,padx=5,pady=5)
        self.button_say_english.grid(row = 0,column = 2,padx=0,pady=5)
        self.button_translate.grid(row = 1,column = 4)
        self.button_clear.grid(row = 0,column = 3)
        self.button_check.grid(row = 0,column = 4)
        self.button_translate.bind("<ButtonRelease-1>",self.translateListener)
        self.button_clear.bind("<ButtonRelease-1>",self.clearListener)
        self.button_say_chinese.bind("<ButtonRelease-1>",self.sayChineseListener)
        self.button_say_english.bind("<ButtonRelease-1>",self.sayEnglishListener)

    #call api
    def translateListener(self,event):
        #translateService.TranslateService.say(self.text_source.get(0.0,END))
        sourceContent = self.text_source.get(0.0,END)
        if sourceContent.strip()=="":
            tkinter.messagebox.showinfo("messagebox","The left text cannot be empty ! ")
            return

        #Translating
        self.button_translate['state'] = DISABLED
        self.button_translate.config(text='translating ...')
        self.__service.translate(sourceContent,self.callbackTarget)



    # clear text info
    def clearListener(self,event):
        self.text_source.delete(0.0, END)
        self.text_target.delete(0.0, END)

    def sayChineseListener(self,event):
        self.text_source.delete(0.0, END)
        self.text_target.delete(0.0, END)
        self.button_say_chinese['state'] = DISABLED
        self.button_say_english['state'] = DISABLED
        self.__speech.recordAndRecognize("zh",self.callbackSpeech,5)
        #录音时长为5秒
        #source=speechRecognize.recordAndRecognize("zh",5)
        #self.text_source.insert(0.0, source)


    def sayEnglishListener(self,event):
        self.text_source.delete(0.0, END)
        self.text_target.delete(0.0, END)
        self.button_say_chinese['state'] = DISABLED
        self.button_say_english['state'] = DISABLED
        self.__speech.recordAndRecognize("en",self.callbackSpeech,5)
        #录音时长为5秒
        #source=speechRecognize.recordAndRecognize("en",5)
        #self.text_source.insert(0.0, source)



        # call back when get result
    def callbackTarget(self,content):
        self.text_target.delete(0.0, END)
        self.text_target.insert(0.0, content)
        self.button_translate['state'] = ACTIVE
        self.button_translate.config(text='auto translation')


    def callbackSpeech(self,language,result):
        self.button_say_chinese['state'] = ACTIVE
        self.button_say_english['state'] = ACTIVE
        self.text_source.insert(0.0, result)

        status = self.var1.get()
        #Translating
        if status == 1:
            self.button_translate['state'] = DISABLED
            self.button_translate.config(text='translating ...')
            sourceContent = self.text_source.get(0.0,END)
            if sourceContent.strip()=="":
               print('The left text cannot be empty !')
            else:
                self.__service.translate(sourceContent,self.callbackTarget)


frame = Application()