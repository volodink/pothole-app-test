from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.loader import Logger


class CamApp(App):
    def build(self):
        self.img1 = Image(size_hint=(1,.8))
        self.button = Button(text="Verify", size_hint=(1,.1))
        self.verification = Label(text="Verification Uninitialized", size_hint=(1,.1))

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.img1)
        layout.add_widget(self.verification)
        layout.add_widget(self.button)

        return layout

if __name__ == '__main__':
    CamApp().run()

