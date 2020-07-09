from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.factory import Factory
import subprocess
import csv

with open("out.csv", "r") as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)

Builder.load_string(
    """
<MainScreen>:
    GridLayout:
        cols: 2
        Button:
            text: "Show correlations"
            on_release:
                app.manage_screens("correlation_attributes", "add")
                app.change_screen("correlation_attributes")
        Button:
            text: "Show Transition visualisation"
            on_release: app.open_visualisation('transition_model.py')
        Button:
            text: "Show hair length before haircut visualisation"
            on_release: app.open_visualisation('hairbeforemodel.py')
        Button:
            text: "Show Hair style visualisation"
            on_release: app.open_visualisation('hairstylemodel.py')
        Button:
            text: "Show Barber visualisation"
            on_release: app.open_visualisation('barbermodel.py')
        Button:
            text: "Show Customer reaction visualisation"
            on_release: app.open_visualisation('reactionmodel.py')
        Button:
            text: "Show Skin tone visualisation"
            on_release: app.open_visualisation('skintonemodel.py')
        Button:
            text: "Show Styling time visualisation"
            on_release: app.open_visualisation('stylingtime.py')
        
        Button:
            text: "Show Weather condition visualisation"
            on_release: app.open_visualisation('weathermodel.py')
        Button:
            text: "Show data"
            on_release:
                app.manage_screens("view_data", "add")
                app.change_screen("view_data")

<CorrelationAttributes@Screen>:
    on_enter: app.them_buttons(bx_btns, selected)
    GridLayout:
        cols: 1
        rows: 4
        BoxLayout:
            size_hint_y: 0.2
            Label:
                text: "Click attributes to identify patterns in"
        BoxLayout:
            size_hint_y: 1
            GridLayout:
                rows: 2
                id: bx_btns
        BoxLayout:
            size_hint_y: 0.1
            Button:
                text: "Click to find patterns..."
                on_release:
                    app.show_patterns()
            Button:
                text: "Return to previous screen"
                on_release:
                    app.manage_screens("correlation_attributes", "remove")
                    app.change_screen("main")
        BoxLayout:
            size_hint_y: 0.5
            GridLayout:
                id: selected
                rows: 3


<ViewData@Screen>:
    on_enter: app.viewing(bx)
    BoxLayout:
        Button:
            
    BoxLayout:
        id: bx
        orientation: "vertical"     
"""
)


class MainScreen(Screen):
    pass


class DWMBarberShop(App):
    selected_attrs = []

    def viewing(self, bx):
        count = 0
        for entry in data:
            if count > 10:
                return
            s = ", ".join(entry)
            s = s + "\n"
            bx.add_widget(Label(text=s))
            count += 1

    def them_buttons(self, ref, ref2):
        self.ref2 = ref2
        a = [
            "Hair Style Name",
            "Normal Price (N$)",
            "Barber",
            "Weather",
            "Environment Noise Level",
            "Head Shape",
            "Customer Reaction",
            "Discount Percent",
            "Age Group",
            "Pre Hair Length",
            "Physical Height (m)",
            "Body Mass (kg)",  # in age group +/- 5
            "Date (DDMMYYYY)",
            "Client Skin Tone",
            "Styling Time (minutes)",  # in style +/- 10
        ]
        for n in a:
            ref.add_widget(Button(text=n, on_release=self.btn_action))

    def btn_action(self, bt):
        self.selected_attrs.append(bt.text)
        self.ref2.add_widget(Label(text=bt.text))

    def show_patterns(self):
        s = ""
        for n in self.selected_attrs:
            s += f'"{n}" '
        import os

        a = os.path.join(os.getcwd(), "correlation_.py")
        f = a + " " + s
        print(f)
        subprocess.Popen(f, close_fds=True, shell=True)

    def open_visualisation(self, p):
        subprocess.Popen("python " + p, close_fds=True)

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name="main"))
        return self.sm

    def manage_screens(self, screen_name, action):
        scns = {
            "main": MainScreen,
            "correlation_attributes": Factory.CorrelationAttributes,
            "view_data": Factory.ViewData,
        }

        if action == "remove":
            if self.sm.has_screen(screen_name):
                self.sm.remove_widget(self.sm.get_screen(screen_name))
            # print("Screen ["+screen_name+"] removed")
        elif action == "add":
            if self.sm.has_screen(screen_name):
                print("Screen [" + screen_name + "] already exists")
            else:
                self.sm.add_widget(scns[screen_name](name=screen_name))
                print(screen_name + " added")
                # print("Screen ["+screen_name+"] added")

    def change_screen(self, screen_name):
        if self.sm.has_screen(screen_name):
            self.sm.current = screen_name
        else:
            print("Screen [" + screen_name + "] does not exist.")


DWMBarberShop().run()
