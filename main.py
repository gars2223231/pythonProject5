from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config


Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 700)
Config.set('graphics', 'height', 500)

class BoxApp(App):


    def build(self):
        bl = BoxLayout(orientation ='vertical', padding =[100], spacing = 10)

        bl.add_widget(Button(text = 'Начать', on_press = self.click))
        bl.add_widget(Button(text='Настройки', on_press = self.click))
        bl.add_widget(Button(text='Инфо ', on_press = self.click))
        return bl


    def click(self, instance):
        pass






if __name__ == '__main__':
    BoxApp().run()