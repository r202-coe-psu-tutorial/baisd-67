import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        layout = BoxLayout(orientation="vertical")

        # begin add first layer
        first_layer = BoxLayout(orientation="horizontal")
        first_layer.add_widget(Label(text="Username"))
        self.username_input = TextInput(
            hint_text="Enter your name here",
        )

        first_layer.add_widget(self.username_input)
        layout.add_widget(first_layer)

        # begin add second layer
        second_layer = BoxLayout(orientation="horizontal")
        second_layer.add_widget(Label(text="Password"))

        self.password_input = TextInput(hint_text="Password", password=True)
        second_layer.add_widget(self.password_input)
        layout.add_widget(second_layer)

        # add button to layout
        layout.add_widget(Button(text="Login", on_press=self.login_callback))
        return layout

    def login_callback(self, instance):
        print("Login button pressed")

        if self.username_input.text == "admin" and self.password_input.text == "admin":
            print("Login successful")
        else:
            print("Login failed")


if __name__ == "__main__":
    MyApp().run()
