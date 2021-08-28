# coding = utf8
import os

os.path.abspath(".")

from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button


class PageLayoutWidget(PageLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn1 = Button(text="Button_Bro1", background_color=[0.2, 0.5, 0.9, 1])
        btn2 = Button(text="Button_Bro2", background_color=[0.2, 0.1, 0.5, 1])
        btn3 = Button(text="Button_Bro3", background_color=[0.8, 0.8, 0.6, 1])
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)

    def say_hello(self):
        print("Hello")


class PageApp(App):
    def build(self):
        return PageLayoutWidget()


if __name__ == '__main__':
    PageApp().run()
