# coding = utf8
import os

os.path.abspath("..")
"""
    @File:sizeApp.py
    @Author:Bruce
    @Date:2021/7/31
"""
# 导入Kivy的App类，它是所有Kivy应用的基类
from kivy.app import App
# 引入布局
from kivy.uix.floatlayout import FloatLayout


# 布局类
class SizeFloat(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# 继承基类
class SizeApp(App):
    # 实现App类的build()方法(继承自App类)
    def build(self):
        # 返回根控件
        return SizeFloat()


"""
    pos_hint:传入字典值，如下可取：
    1、x->{"x":0.5,"y":0.5}
    2、center_x->as 1
    3、right->as 1
    4、y->as 1
    5、center_y->as 1
    6、top->as 1
"""

# 程序入口
if __name__ == '__main__':
    SizeApp().run()
