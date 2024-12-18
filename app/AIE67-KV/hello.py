import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(BoxLayout):
    def login_callback(self, username, password):

        print("Login button pressed", username, password)

        if username == "admin" and password == "admin":
            print("Login successful")
        else:
            print("Login failed")


class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    MyApp().run()
