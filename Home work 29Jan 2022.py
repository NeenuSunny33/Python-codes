import os
import glob

from PyPDF2 import PdfFileMerger
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

path = "C://Users//Neenu Sunny//Neenu"

class ButtonPressApp(App):

   def __init__(self):
      super(ButtonPressApp, self).__init__()
      self.btn = Button(text='List of directories')
      self.btn1= Button(text='List of Pdf')
      self.btn2 = Button(text='Merged PDF file')

   def build(self):
      self.btn.bind(on_press=self.click_event)
      self.btn1.bind(on_press=self.click_event1)
      self.btn2.bind(on_press=self.click_event2)
      layout = BoxLayout()
      layout.orientation = 'vertical'
      layout.add_widget(self.btn)
      layout.add_widget(self.btn1)
      layout.add_widget(self.btn2)
      return layout


   def click_event(self, btn):

       dir_list = os.listdir(path)
       print("Files and directories in '", path, "' :",dir_list)

   def click_event1(self, btn1):
       file1=[]

       for file in os.listdir(path):
           if file.endswith('pdf'):
               file2.append(file)
            p=len(file1)
       try:
           if p !=0:
              print("Pdf files are :" ,file1)
       except:
           print("no pdf files available")

   def click_event2(self, btn2):

       merger = PdfFileMerger()

       file2 = []
       for file in  os.listdir(path):
           if file.endswith('pdf'):
               file2.append(file)
       q = len(file2)
       print(q)

       if q > 1:
           for item in os.listdir(path):
               if item.endswith('pdf'):
                   merger.append(item)
           merger.write("C://Users//Neenu Sunny//Neenu//mergenew.pdf")
           merger.close()
           print("File is merged")
           print("No pdf file")

       elif q == 1:
           print("One pdf file")

       else:
           print("No pdf file")

MainLayout = ButtonPressApp()
MainLayout.run()