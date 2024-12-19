from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget  

class HitTheBossGame(Widget):
    pass 

class HitTheBossApp(App):
    def build(self):
        return HitTheBossGame()

if __name__ == '__main__':
    HitTheBossApp().run()