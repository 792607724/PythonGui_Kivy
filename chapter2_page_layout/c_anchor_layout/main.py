# coding = utf8

import os

os.path.abspath(".")

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color


class AnchorLayoutWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)
        anchor_first = AnchorLayout(anchor_x="left", anchor_y="top")
        anchor_first.add_widget(Button(text="Button_Bro1", size_hint=[1 / 3, 1 / 3]))
        anchor_second = AnchorLayout(anchor_x="right", anchor_y="bottom")
        anchor_second.add_widget(Button(text="Button_Bro2", size_hint=[1 / 3, 1 / 3]))
        self.add_widget(anchor_first)
        self.add_widget(anchor_second)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class AnchorApp(App):
    def build(self):
        return AnchorLayoutWidget()


if __name__ == '__main__':
    AnchorApp().run()
