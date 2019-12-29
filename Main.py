from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.slider import Slider
from kivy.uix.dropdown import DropDown
from kivy.uix.scatter import Scatter
from kivy.graphics import *
from kivy.uix.behaviors import DragBehavior
from math import cos, sin, radians
import re
import function as func
from graphics import Scat
from navdrawer import NavigationDrawer


scatter = None
dec_places = 3
input_list = []
var = 'AB', '∠ACB', 'BC', '∠BAC', 'AC', '∠ABC'
sm = ScreenManager(transition=FadeTransition())

# CREATING 4 MAIN SCREENS AS CLASSES


class Sc1(Screen):            # Calculator
    pass


class Sc2(Screen):            # Graphic
    def __init__(self, **kwargs):
        super(Sc2, self).__init__(**kwargs)
        global scatter
        scatter = Widget(size_hint=(None, None))
        self.ids.graphic.add_widget(scatter)


class Sc3(Screen):            # Converter
    def __init__(self, **kwargs):
        super(Sc3, self).__init__(**kwargs)

        # DEFINING VARS
        scales = ['Length', 'Speed']
        m = [['Kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Micrometer', 'Nanometer', 'Picometer'],
             ['km/h', 'm/h', 'km/s', 'm/s']]
        rows = BoxLayout(spacing=10, orientation='vertical', height=dp(45*len(scales)), size_hint_y=None)

        # CREATING ROWS
        for i in range(len(scales)):
            row = BoxLayout(orientation='horizontal', spacing=10)
            row.add_widget(Label(text=scales[i], font_name='assets/unicode.ttf'))
            row.add_widget(FloatInput(font_size=21))
            row.add_widget(DropBut(m[i]))
            row.add_widget(Label(text='[b]INTO[/b]', markup=True))
            row.add_widget(FloatInput(font_size=21))
            row.add_widget(DropBut(m[i]))
            row.add_widget(Button(text='Convert'))
            rows.add_widget(row)

        self.ids.conv.add_widget(rows)
        self.ids.conv.add_widget(Widget())


class Sc4(Screen):            # About
    def __init__(self, **kwargs):
        super(Sc4, self).__init__(**kwargs)
        file = open("about.txt", 'r')
        about = file.read()
        file.close()
        self.ids.box.add_widget(Label(text=about, size_hint=(1, 0.5), valign='top', halign='center'))
        self.ids.box.add_widget(Widget())

# CREATING AUXILIARY CLASSES


class DropBut(Button):
    def __init__(self, metrics, **kwargs):
        super(DropBut, self).__init__(**kwargs)
        dropdown = DropDown()
        for word in metrics:
            but = Button(text=word, size_hint_y=None, height=44)
            but.bind(on_release=lambda but: dropdown.select(but.text))
            dropdown.add_widget(but)
        self.text = ' Unitsв‡©'
        self.font_name = 'assets/unicode.ttf'
        self.width = dp(100)
        self.size_hint_x = None
        self.background_color = (0, 0, 0, 0)
        self.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self, 'text', x))


class FloatInput(TextInput):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        self.multiline = False
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)


class Butt(ButtonBehavior, Image):

    def __init__(self, **kwargs):
        super(Butt, self).__init__(**kwargs)
        self.source = 'assets/ham2.png'

    def on_press(self):
        self.source = 'assets/ham1.png'

    def on_release(self):
        self.source = 'assets/ham2.png'


class Settings(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)
        self.source = 'assets/settings1.png'

    def on_press(self):
        self.source = 'assets/settings.png'
        sett = Popup(title='Settings', size_hint=(0.8, 0.8))

        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text="Choose how many decimal places do you want?"))

        dec_pla = BoxLayout()
        for i in range(4):
            dec_pla.add_widget(Label(text=str(i)))
            dec_pla.add_widget(Widget())
        else:
            dec_pla.add_widget(Label(text='4'))

        content.add_widget(dec_pla)
        slider = Slider(step=25, value=dec_places*25, on_press=lambda j: upd())
        slider.bind(on_press=lambda j: sett.dismiss())
        content.add_widget(slider)

        def upd():
            global dec_places
            dec_places = int(slider.value / 25)

        submit = Button(text="Submit", on_press=lambda j: upd())
        submit.bind(on_press=lambda j: sett.dismiss())
        content.add_widget(submit)

        sett.add_widget(content)
        sett.open()

    def on_release(self):
        self.source = 'assets/settings1.png'


class Calculator(BoxLayout):
    global toch

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.screen_manager = sm

        def sol():
            for j in range(6):
                if input_list[j].text == '':
                    input_list[j].text = '0'

            results = func.calc(float(input_list[2].text), float(input_list[4].text), float(input_list[0].text),
                              float(input_list[3].text), float(input_list[5].text), float(input_list[1].text))
            # -----------------------
            if not (results[0] and results[1] and results[2] and results[3] and results[4] and results[5]):
                popup = Popup(title='Oooops, Something went wrong', content=Button(
                    text='OK', size_hint=(0.8, 0.8), on_release=lambda n: popup.dismiss()), size_hint=(0.5, 0.25))
                for j in range(6):
                    input_list[j].text = ''
                popup.open()
                return

            for j in range(6):
                if input_list[j].text == '0':
                    input_list[j].foreground_color = 0.18, 0.62, 0.38, 1
                input_list[j].text = str(round(results[j], dec_places))

            # -----------------------
            # -----------------------
            global goto_graphics, erase
            goto_graphics = Button(text='Switch To Graphics', size_hint=(0.8, 1), font_size=20,
                                   on_release=lambda d: draw_one(results))
            erase = Button(text="Reset", font_size=20, on_press=lambda d: clear(), size_hint=(0.2, 1))
            buttons.remove_widget(example)
            if 1 == len(buttons.children):
                buttons.add_widget(goto_graphics)
                buttons.add_widget(erase)

            def draw_one(points):
                global scatter
                scatter.add_widget(Scat(points))
                switch("Graphics", 0)

        # -----------------------
            #global toch
            #toch = (pox, poy, pox + a, poy, pox + cos(radians(be)) * c, poy + sin(radians(be)) * c)

        def clear():
            buttons.clear_widgets()
            buttons.add_widget(Button(text='Calculate', size_hint=('1', '0.1'), font_size=20, on_release=lambda a: sol()
                                      ))
            buttons.remove_widget(erase)
            buttons.remove_widget(goto_graphics)
            buttons.add_widget(example)
            for k in range(6):
                input_list[k].text = ''
                input_list[k].foreground_color = 0, 0, 0, 1

        # -------------------------

        global bl
        bl = BoxLayout(orientation='vertical', spacing=5, padding=5)
        gl = GridLayout(cols=2, spacing=2, size_hint=('1', '0.5'))
        # -------------------------
        ###################################################################
        global navdraw
        navdraw = NavigationDrawer()

        def set_anim_type(name):
            navdraw.anim_type = name

        def set_transition(name):
            navdraw.opening_transition = name
            navdraw.closing_transition = name

        def switch(p, r):
            if r:
                navdraw.toggle_state(True)
            self.screen_manager.current = p

        set_anim_type('slide_above_anim')
        set_transition('linear')
        panel = BoxLayout(orientation='vertical')
        panel.add_widget(Button(text='Calculator', on_press=lambda b: switch("Calculator", 1), background_color=(0, 0,
                                                                                                                 0, 0)))
        panel.add_widget(Button(text='Graphics', on_press=lambda a: switch("Graphics", 1), background_color=(0, 0, 0,
                                                                                                             0)))
        panel.add_widget(Button(text='Converter', on_press=lambda a: switch("Converter", 1), background_color=(0, 0, 0,
                                                                                                               0)))
        # panel.add_widget(Button(text='Tips', background_color=(0, 0, 0, 0)))
        panel.add_widget(Button(text='About', on_press=lambda a: switch("About", 1), background_color=(0, 0, 0, 0)))
        navdraw.add_widget(panel)
        ##################################################################
        header = BoxLayout(size_hint_y=None, height=dp(55), padding=8)
        header.add_widget(Butt(size_hint=(0.05, 1), on_press=lambda j: navdraw.toggle_state()))
        header.add_widget(Label(text='[b]TRIGOMA[/b]', markup=True))
        header.add_widget(Settings(size_hint=(0.05, 1)))
        bl.add_widget(header)

        for i in range(6):
            gl.add_widget(Label(text=var[i], font_name='assets/cambria.ttc', font_size=25))
            input_list.append(FloatInput(font_size=21))
            gl.add_widget(input_list[i])
        input_list[0].focus = True
        bl.add_widget(gl)

        global buttons
        buttons = GridLayout(cols=3, spacing=2, size_hint=(1, 0.1))
        buttons.add_widget(Button(text='Calculate', size_hint=('1', '0.1'), font_size=20, on_release=lambda a: sol()))
        example = Image(source='assets/triangle.png')
        buttons.add_widget(example)

        bl.add_widget(buttons)
        navdraw.add_widget(bl)
        self.add_widget(navdraw)


class Main(App):
    def build(self):
        sm.add_widget(Sc1(name='Calculator'))
        sm.add_widget(Sc2(name='Graphics'))
        sm.add_widget(Sc3(name='Converter'))
        sm.add_widget(Sc4(name='About'))
        return sm


if __name__ == "__main__":
    Main().run()
