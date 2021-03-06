# coding = utf8
import os

os.path.abspath("..")
"""
    @File:floatLayoutApp.py
    @Author:Bruce
    @Date:2021/7/31
"""
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class FloatLayoutWidget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FloatLayoutApp(App):
    def build(self):
        return FloatLayoutWidget()


if __name__ == '__main__':
    FloatLayoutApp().run()
