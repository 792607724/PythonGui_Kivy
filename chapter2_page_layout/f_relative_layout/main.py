# coding = utf8
import os

os.path.abspath(".")

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color


class MyButton(Button):
    # 自定义控件类
    """
        自定义一个按钮，提出公共属性
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
