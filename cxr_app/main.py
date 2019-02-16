from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.properties import (ListProperty,
                             StringProperty,
                             NumericProperty)

import os
import random
import glob
import csv

def _format(str):
    return round(float(str), 1)

def load_cxr_paths(root_path, csv_file):
    root_img_path = os.path.join(os.getcwd(), root_path, 'images')
    root_csv_path = os.path.join(os.getcwd(), root_path, csv_file)
    avail_imgs = os.listdir(root_img_path)
    entries = []

    with open(root_csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Image Index'] in avail_imgs:
                entries.append({'img': os.path.join(root_img_path, row['Image Index']) ,
                'finding':row['Finding Label'],
                'BBox':[_format(row['Bbox [x']),
                       _format(row['y']),
                       _format(row['w']),
                       _format(row['h]'])]})
    return entries

class ImageViewer(BoxLayout):

    cxr_source = StringProperty('doge1.jpg')
    cxr_finding = StringProperty('')
    visibility = NumericProperty(0)
    finding_coords = ListProperty([0,0,0,0])
    img_arry = load_cxr_paths('ChestX-ray8', 'BBox_List_2017.csv')

    def show_finding(self, *args):
        self.visibility = 1

    def load_new_cxr(self, *args):
        cxr_selection = self.img_arry[random.randint(1, len(self.img_arry) - 1)]
        self.cxr_source = cxr_selection['img']
        self.cxr_finding = cxr_selection['finding']
        # self.finding_coords = cxr_selection['BBox']
        print (cxr_selection['BBox'])
        self.visibility = 0

class CXRApp(App):
    def build(self):
        return ImageViewer()

if __name__ == '__main__':
    CXRApp().run()
