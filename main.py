# coding = utf8

import os

os.path.abspath(".")

# 导入Kivy的App类，它是所有Kivy应用的基类
from kivy.app import App

# Kivy内置了丰富的控件（widget），如按钮（button），复选框（checkbox），标签（label），输入框（textinput），滚动容器（scrollable container）

# 引入BoxLayout布局
from kivy.uix.boxlayout import BoxLayout


class IndexPage(BoxLayout):

    # 初始化
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # # 添加一个按钮
        # self.join = Button(text="Hello World")
        # 将按钮添加到页面控件中
        # self.add_widget(self.join)


# 从App类中继承了Kivy应用最基本的方法，如创建窗口，设置窗口大小和位置等
class TestApp(App):
    # 实现TestApp类的build方法（继承自App类）
    def build(self):
        # build方法返回的控件，自Kivy中，称之为根控件root widget
        # kivy将自动缩放根控件，让它填满整个窗口
        return IndexPage()


if __name__ == '__main__':
    TestApp().run()
    print("Kivy")
