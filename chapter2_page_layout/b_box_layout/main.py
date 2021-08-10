# coding = utf8

import os

os.path.abspath(".")

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
from kivy.app import App


class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        with self.canvas:
            Color(1, 1, 1, 1)
        self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.add_widget(Button(text="Button_1"))
        self.add_widget(Button(text="Button_2"))

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class BoxApp(App):
    def build(self):
        return BoxLayoutWidget()


if __name__ == '__main__':
    BoxApp().run()
