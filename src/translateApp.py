# -*- coding: UTF-8 -*-
from tkinter import *
from translateService import *

class Application:

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 180
    TITLE = "Online Translation"

    def __init__(self):
        self.frame = Tk()
        self.__service = TranslateService()
        self.frame.title(Application.TITLE)
        self.frame.maxsize(Application.WINDOW_WIDTH, Application.WINDOW_HEIGHT)
        self.frame.minsize(Application.WINDOW_WIDTH, Application.WINDOW_HEIGHT)
        self.createSourceText()
        self.createTargetText()
        self.createButton()
        self.frame.mainloop()

    def createSourceText(self):
        self.text_source = Text(self.frame,height = "8",width = 40)
        self.text_source.grid(row = 1,column = 1,columnspan=3,rowspan =2,padx=10,pady=10)

    def createTargetText(self):
        self.text_target = Text(self.frame,height = "8",width = 40)
        self.text_target.grid(row = 1,column = 8,columnspan=3,rowspan =2,padx=10,pady=10)

    def createButton(self):
        self.button_say_chinese = Button(self.frame,text = "say chinese",width = 10)
        self.button_say_english = Button(self.frame,text = "say english",width = 10)
        self.button_translate = Button(self.frame,text = "English --> Chinese",width = 20)
        self.button_clear = Button(self.frame,text = "clear",width = 20)
        self.button_say_chinese.grid(row = 0,column = 1,padx=5,pady=5)
        self.button_say_english.grid(row = 0,column = 2,padx=0,pady=5)
        self.button_translate.grid(row = 1,column = 4)
        self.button_clear.grid(row = 2,column = 4)
        self.button_translate.bind("<ButtonRelease-1>",self.translateListener)
        self.button_clear.bind("<ButtonRelease-1>",self.clearListener)
        self.button_say_chinese.bind("<ButtonRelease-1>",self.sayChineseListener)
        self.button_say_english.bind("<ButtonRelease-1>",self.sayEnglishListener)

    #call api
    def translateListener(self,event):
        #translateService.TranslateService.say(self.text_source.get(0.0,END))
        result = self.__service.translate(self.text_source.get(0.0,END))
        self.text_target.delete(0.0, END)
        self.text_target.insert(0.0, result)

    # clear text info
    def clearListener(self,event):
        self.text_source.delete(0.0, END)
        self.text_target.delete(0.0, END)


    def sayChineseListener(self,event):
        self.text_source.delete(0.0, END)
        self.text_target.delete(0.0, END)
        self.text_source.insert(0.0, '中国')


    def sayEnglishListener(self,event):
        self.text_source.delete(0.0, END)
        self.text_target.delete(0.0, END)
        self.text_source.insert(0.0, 'china')

frame = Application()