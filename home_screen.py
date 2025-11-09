from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.graphics import Color, Line
import time
import json
import add_load_data

class HomeScreen(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
    def on_button_press(self,value):
        if value == "yes":
            print("wow u pressed the button!")

    def on_enter(self, *args):
        layout = self.ids.main_box
        
        add_load_data.initializeJson()
        with open("data.json", "r") as f:
            data = json.load(f)
            if len(data["users"]) == 0:
                check_users = self.ids.no_one
                if check_users not in layout.children:
                    if check_users.parent is None:
                        layout.add_widget(check_users)

            else:
                
                try:
                    if self.ids.no_one.parent:
                        names = add_load_data.getNames()
                        for name in names:
                            self.add_name(name,save_to_json=False)
                        layout.remove_widget(self.ids.no_one)
                except ReferenceError:
                    pass # widget was deleted so reference error occurred which is now passed

                    
    
    def show_name_popup(self):
    # create a new layout just for the popup
        popup_layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        input_field = TextInput(hint_text="Enter name", multiline=False)
        popup_layout.add_widget(input_field)

        # popup butons
        btn_box = BoxLayout(size_hint_y=None, height=40, spacing=10)
        ok_btn = Button(text="OK")
        cancel_btn = Button(text="Cancel")
        btn_box.add_widget(ok_btn)
        btn_box.add_widget(cancel_btn)
        popup_layout.add_widget(btn_box)

        # create popup
        popup = Popup(title="Enter Name", content=popup_layout,
                    size_hint=(0.8, 0.4), auto_dismiss=False)

        ok_btn.bind(on_release=lambda x: self.add_name(input_field.text, popup,save_to_json=True))
        cancel_btn.bind(on_release=popup.dismiss)

        popup.open()
        

    def save_price(self):
        inner = self.ids.users_list
        toggled_buttons = [btn.text for btn in inner.children if isinstance(btn, ToggleButton) and btn.state == 'down']
        try:
            try:
                price = float(self.ids.price_input.text)
                price = price / len(toggled_buttons)
                for name in toggled_buttons:
                    add_load_data.setPrice(name,float(price))
                self.ids.price_input.text = "Tally Saved!"
            except ValueError:
                self.ids.price_input.text = "Enter A Number!"

        except ZeroDivisionError:
            self.ids.price_input.text = "Select A User First!"
        
    def add_name(self, name, popup=None,save_to_json=False):
        if name.strip():  # only if not empty
            inner = self.ids.users_list
            if save_to_json:
                add_load_data.addNewName(name)
                if len(add_load_data.getNames()) > 0:
                    layout = self.ids.main_box
                    check_users = self.ids.no_one
                    layout.remove_widget(check_users)


            new_btn = ToggleButton(
                text=name,
                font_name="assets/Rhigen.otf",
                size_hint_y=0.3,
                pos_hint={'center_x': 0.5, 'top': 0.5},
                size_hint_x=None,
                width=150,
                color=(0, 0, 0, 1),
                background_normal='',   
                background_color=(1, 1, 0.962, 1),  
            )

            
            with new_btn.canvas.after:
                Color(0, 0, 0, 1)  # border color (black)
                new_btn.border_line = Line(
                    rectangle=(new_btn.x, new_btn.y, new_btn.width, new_btn.height),
                    width=1.3
                )

            
            def update_border(instance, *args):
                instance.border_line.rectangle = (instance.x, instance.y, instance.width, instance.height)

            new_btn.bind(pos=update_border, size=update_border)

            def on_state_change(instance, value):
                if value == 'down':
                    instance.background_color = (0.3, 0.5, 0.3, 1)
                    instance.color = (1,1,1,1)  
                else:
                    instance.background_color = (1, 1, 0.962, 1)      
                    instance.color = (0,0,0,1) 

            new_btn.bind(state=on_state_change)
            inner.add_widget(new_btn)

        if popup and getattr(popup, "parent", None):
            popup.dismiss()
