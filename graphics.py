from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.bubble import Bubble, BubbleButton
from math import cos, sin, radians
from kivy.graphics import Color, Triangle, Rectangle, Line
from random import random

"""var = 'AB', '∠ACB', 'BC', '∠BAC', 'AC', '∠ABC'
"""


class BubbleWidget(Bubble):
    def __init__(self, layout, widget, points, **kwargs):
        super(BubbleWidget, self).__init__(**kwargs)

        self.size_hint = (None, None)
        self.size = (120, 30)
        self.pos_hint = {'center_x': .5, 'center_y': .6}
        self.add_widget(BubbleButton(text='Clone', on_release=lambda a: layout.add_widget(Scat(layout, points))))
        self.add_widget(BubbleButton(text='Delete', on_release=lambda a: layout.remove_widget(widget)))
        # self.add_widget(BubbleButton(text='...', size_hint=(0.5, 1)))


class Scat(Scatter):
    def __init__(self, layout, points, **kwargs):
        super(Scat, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (points[2], points[5])
        self.add_widget(TriangleClass(points, layout, self))


class TriangleClass(Widget):
    def __init__(self, points, layout, widget, **kwargs):
        super(TriangleClass, self).__init__(**kwargs)
        self.points = points
        with self.canvas:
            Color(random(), random(), random(), 1)
            Triangle(points=points)
        self.bubb, self.bubb_is = BubbleWidget(layout, widget, self.points), 0

    def on_touch_up(self, touch):
        curve = Line(points=self.points, width=2, close=True)
        if touch.is_double_tap:
            if not self.bubb_is:
                self.add_widget(self.bubb)
                self.bubb_is = 1
                self.canvas.add(curve)

                    # Color(0.5, 0.5, 0.3, 1)
            else:
                self.canvas.remove(curve)
                self.bubb_is = 0
                self.remove_widget(self.bubb)


if __name__ == "__main__":
    from kivy.app import App


    class Main(App):
        def build(self):
            main = BoxLayout(orientation='vertical')
            points = (3000.0, 36.86989764584401, 4000.0, 53.13010235415599, 5000.0, 90.0)
            x_offset = 0
            y_offset = 0
            width = 150  # points[2]
            height = 150  # points[0]

            points = [x_offset, y_offset, x_offset + width, y_offset, x_offset + cos(radians(points[5])) * height,
                      y_offset + sin(radians(points[5])) * height]

            main.add_widget(Button(text='Spawn a triangle', on_release=lambda a: sec.add_widget(Scat(sec, points))))
            sec = Widget()
            # main.add_widget(Scat([3, 60.0, 3, 60.0, 3, 60.0]))
            main.add_widget(sec)

            return main
    Main().run()
