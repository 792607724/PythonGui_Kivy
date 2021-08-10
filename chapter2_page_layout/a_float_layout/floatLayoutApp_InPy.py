# coding = utf8
import os

os.path.abspath(".")
"""
    @File:floatLayoutApp_InPy.py
    @Author:Bruce
    @Date:2021/7/31
"""

"""
    FloatLayout是浮动布局，它允许将子部件通过位置和尺寸放置在窗口的任意位置
    可以保证应用不会因为窗口的大小改变，而布局乱作一团
"""
# Py内引用布局
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color


class FloatLayoutApp_InPy(App):
    def build(self):
        def update_rect(layout, *args):
            """设置背景尺寸，可忽略"""
            layout.rect.pos = layout.pos
            layout.rect.size = layout.size

        float_layout = FloatLayout()
        # 设置背景颜色（可忽略）
        with float_layout.canvas:
            Color(1, 1, 1, 1)
        float_layout.rect = Rectangle(pos=float_layout.pos, size=float_layout.size)
        float_layout.bind(pos=update_rect, size=update_rect)
        # 在布局内的size_hint:0.3,0.2处添加一个尺寸为0.3,0.2的按钮
        button = Button(text="Hello FloatLayoutApp_InPy", size_hint=(0.3, 0.2),
                        pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=(0.8, 0.9, 0.2, 1))
        # 将按钮添加到布局内
        float_layout.add_widget(button)
        # 返回布局
        return float_layout


if __name__ == '__main__':
    FloatLayoutApp_InPy().run()
