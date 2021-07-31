# coding = utf8
import os

os.path.abspath(".")
"""
    @File:posApp.py
    @Author:Bruce
    @Date:2021/7/31
"""
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class PosFloat(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PosApp(App):
    def build(self):
        return PosFloat()


if __name__ == '__main__':
    PosApp().run()
