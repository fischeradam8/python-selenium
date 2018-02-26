#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from ttk import *
from Tkinter import *


class App():
    def __init__(self):
        self.root = Tk()
        text_widget = Text(self.root, height=1, width=30)
        text_widget.pack()
        text_widget.insert(END, 'Mennyire van még meg az F5-öd?')
        modes = [
            ("Még van rajta felirat", 5),
            ("Kopott, és kattog", 20),
            ("Már nincs köztünk", 30),
            ("Már az ujjamról is lemállott a hús!", 100),
        ]

        self.v = IntVar()

        for text, mode in modes:
            b = Radiobutton(self.root, text=text,
                            variable=self.v, value=mode, command=self.close, indicatoron=0)
            b.pack(anchor=W)

        mainloop()

    def close(self):
        print(self.v.get())
        self.root.destroy()
        self.refresher()

    def refresher(self):
        url = 'https://www.google.com'
        browser = webdriver.Chrome()
        browser.get(url)
        for x in range(self.v.get()):
            time.sleep(0.5)
            browser.refresh()


app = App()




