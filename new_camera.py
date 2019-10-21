# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:11:03 2019

@author: ABARNA DEVI
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:51:28 2019

@author: ABARNA DEVI
"""

  
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from predict_final import final

Builder.load_string('''
<CaputeImage>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (720, 480)
        play: True
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CaputeImage(BoxLayout):

    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''

        camera = self.ids['camera']
        camera.export_to_png("IMG.png")
        print("Captured")
        self.ids['camera'].play = False
        self.clear_widgets()
        self.main()

    def main(self):
        string = final.disease("IMG.png")
        print(string)
        self.add_widget(Label(text=string, text_size=(600, None), line_height=1.5))


class Plant_disease_detector(App):

    def build(self):
        return CaputeImage()

if __name__ == "__main__":
    Plant_disease_detector = Plant_disease_detector()
    Plant_disease_detector.run()