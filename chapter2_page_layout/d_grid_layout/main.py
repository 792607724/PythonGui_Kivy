# coding = utf8
import os

os.path.abspath(".")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color


class GridLayoutWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.cols = 3
        for i in range(6):
            btn = Button(text=str(i))
            self.add_widget(btn)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class GridApp(App):
    def build(self):
        return GridLayoutWidget()


if __name__ == '__main__':
    GridApp().run()
