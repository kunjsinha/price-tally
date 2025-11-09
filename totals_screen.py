from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
import add_load_data
import download_logs

class TotalsScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # store references to price labels so we can update them later
        self.price_labels = {}

    def on_enter(self, *args):
        names = add_load_data.getNames()
        layout1 = self.ids.totals_box  # The main vertical layout

        layout1.clear_widgets()
        self.price_labels.clear()

        for name in names:
            price = str(round(add_load_data.getPrice(name), 1))

            # horizontal row for each user
            row = BoxLayout(orientation="horizontal", spacing=20, size_hint_y=None, height=80)

            # Name label
            name_label = Label(
                text=name,
                font_size=40,
                color=(0, 0, 0, 1),
                font_name="assets/wheaton capitals.otf",
                size_hint_x=0.3,
                halign="left",
                valign="middle"
            )
            name_label.bind(size=name_label.setter('text_size'))

            # Price label
            price_label = Label(
                text=price,
                font_size=40,
                color=(0, 0, 0, 1),
                font_name="assets/wheaton capitals.otf",
                size_hint_x=0.3,
                halign="right",
                valign="middle"
            )
            price_label.bind(size=price_label.setter('text_size'))

            # store reference
            self.price_labels[name] = price_label

            # Clear button
            clear_button = Button(
                text="Clear",
                font_size=40,
                color=(0, 0, 0, 1),
                size_hint_x=0.3,
                halign="right",
                valign="middle"
            )
            # use lambda with default argument
            clear_button.bind(on_release=lambda instance, n=name: self.clearPrice(n))

            # Add widgets to row
            row.add_widget(name_label)
            row.add_widget(price_label)
            row.add_widget(clear_button)

            layout1.add_widget(row)

    def clearPrice(self, n):
        """Clears the price for a given user and updates the label."""
        add_load_data.clearPrice(n)
        if n in self.price_labels:
            self.price_labels[n].text = '0'
    
    def download(self):
        download_logs.download_file("data.json")
        