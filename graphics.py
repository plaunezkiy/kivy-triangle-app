from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.uix.bubble import Bubble, BubbleButton
from math import cos, sin, radians
from kivy.graphics import Color, Triangle, Rectangle
from random import random

"""var = 'AB', 'в€ ACB', 'BC', 'в€ BAC', 'AC', 'в€ ABC'
"""


class Scat(Scatter):
    def __init__(self, points, **kwargs):
        x_offset = 50
        y_offset = 50
        points = [x_offset, y_offset, x_offset + points[2], y_offset, x_offset + cos(radians(points[5])) * points[0],
                y_offset + sin(radians(points[5])) * points[0]]

        super(Scat, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (50, 50)
        self.add_widget(TriangleClass(points))


class TriangleClass(Widget):
    def __init__(self, points, **kwargs):
        super(TriangleClass, self).__init__(**kwargs)

        self.size_hint = (None, None)
        self.pos_hint = (None, None)

        with self.canvas:
            Color(random(), random(), random(), 1)
            # Rectangle(size=self.size)
            Triangle(point=points)


if __name__ == "__main__":
    from kivy.app import App


    class Main(App):
        def build(self):
            main = BoxLayout(orientation='vertical')
            main.add_widget(Button(text='Spawn a triangle', on_release=lambda a: sec.add_widget(Scat([3, 60.0, 3, 60.0, 3, 60.0]))))
            sec = Scatter()
            main.add_widget(sec)

            return main
    Main().run()