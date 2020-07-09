from kivy.lang import Builder
from kivy.app import App

root_kv = """
#:import Window kivy.core.window.Window

BoxLayout:
    orientation: "vertical"
    spacing: dp(10)
    BoxLayout:
        size_hint_y: 0.2
        Label:
            text: "Barber Shop System"
            font_size: 30
    
    GridLayout:
        cols: 1
        rows: 2
        GridLayout:
            cols: 2
            BoxLayout:
                size_hint_y: 0.1
                orientation: "horizontal"
                Label:
                    text: "Barber name"
                TextInput:
                    hint_text: "name"
            
            BoxLayout:
                size_hint_y: 0.2
                orientation: "horizontal"
                Label:
                    text: "Hairstyle name"
                TextInput:
                    hint_text: "hairstlye name"

        Button:
            text: "Submit"
            pos_hint: {"center_x": .5}

"""


class MainApp(App):
    def build(self):
        self.root = Builder.load_string(root_kv)


MainApp().run()
