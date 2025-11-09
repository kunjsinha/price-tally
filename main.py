from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from home_screen import HomeScreen
from totals_screen import TotalsScreen
import download_logs


class MainApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition(duration=0.2))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(TotalsScreen(name="totals"))
        return sm
    
if __name__ == "__main__":
    MainApp().run()
