from kivy.app import App
from kivy.uix.button import Button
import random

class RandomNumberApp(App):
    def build(self):
        # Initialize the button with a random number
        self.button = Button(text=str(random.randint(1, 100)))
        # Bind the button's on_press event to the update_number method
        self.button.bind(on_press=self.update_number)
        return self.button

    def update_number(self, instance):
        # When the button is pressed, change its text to another random number
        self.button.text = str(random.randint(1, 100))

if __name__ == '__main__':
    RandomNumberApp().run()