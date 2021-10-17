from kivy.app import App
from kivy.uix.label import Label

class MortgageCalc1App(App):
    def build(self):
        return Label(text="Hello, World")


MortgageCalc1App().run()