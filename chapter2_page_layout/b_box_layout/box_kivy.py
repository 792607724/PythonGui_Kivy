# coding = utf8

import os

os.path.abspath(".")
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BoxApp(App):
    def build(self):
        return BoxLayoutWidget()


if __name__ == '__main__':
    BoxApp().run()
