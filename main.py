from kivy.app import App
from kivy.uix.label import Label


class MortgageCalcApp(App):
    def build(self):
        return Label(text="Hello, World")


MortgageCalcApp().run()