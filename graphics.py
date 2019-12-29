from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.uix.bubble import Bubble, BubbleButton
from math import cos, sin, radians
from kivy.graphics import Color, Triangle, Rectangle
from random import random

"""var = 'AB', '∠ACB', 'BC', '∠BAC', 'AC', '∠ABC'
"""


class BubbleWidget(Bubble):
    def __init__(self, **kwargs):
        super(BubbleWidget, self).__init__(**kwargs)

        self.size_hint = (None, None)
        self.size = (80, 50)
        self.pos_hint: (None, None)

        self.add_widget(BubbleButton(text='Cut', on_release=lambda a: print(134)))
        self.add_widget(BubbleButton(text='Copy'))


class Scat(Scatter):
    def __init__(self, points, **kwargs):
        x_offset = 0
        y_offset = 0
        points = [x_offset, y_offset, x_offset + points[2], y_offset, x_offset + cos(radians(points[5])) * points[0],
                y_offset + sin(radians(points[5])) * points[0]]

        super(Scat, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (100, 100)
        self.add_widget(TriangleClass(points))


class TriangleClass(Button):
    def __init__(self, points, **kwargs):
        self.background_color = (0, 0, 0, 0)
        super(TriangleClass, self).__init__(**kwargs)
        with self.canvas:
            Color(random(), random(), random(), 1)
            Triangle(point=points)

    def on_touch_down(self, touch):
        global bubb
        if touch.is_double_tap:
            print(hasattr(self, 'bubb'))
            if not hasattr(self, 'bubb'):
                self.show_bubble(touch)
            else:
                self.remove_widget(self.bubb)

    def show_bubble(self, touch, *l):
        global bubb
        if not hasattr(self, 'bubb'):
            self.bubb = bubb = BubbleWidget(pos=(touch.x, touch.y))
            self.add_widget(bubb)


if __name__ == "__main__":
    from kivy.app import App


    class Main(App):
        def build(self):
            main = BoxLayout(orientation='vertical')
            main.add_widget(Button(text='Spawn a triangle', on_release=lambda a: sec.add_widget(Scat([3, 60.0, 3, 60.0, 3, 60.0]))))
            sec = Widget()
            main.add_widget(sec)

            return main
    Main().run()
