# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:04:18 2022

@author: Zachery Van Es
"""
import io
import os
import glob
import PySimpleGUI as sg
sg.theme("DarkAmber")

from PIL import Image, ImageTk

file_types = [("JPEG (*.jpg)","*.jpg"),
              ("All files (*.*)","*.*")]

def parse_folder(path):
    images = glob.glob(f'{path}/*.jpg') + glob.glob(f'{path}/*.png')
    return images

def load_image(path, window):
    try:
        image = Image.open(path)
        image.thumbnail((400,400))
        photo_img = ImageTk.PhotoImage(image)
        window["image"].update(data=photo_img)
    except:
        print("Unable to open {path}!")
        
def main():
    elements = [
        [sg.Image(key="image")],
        [
            sg.Text("Folder:"),
            sg.Input(size=(25,1), enable_events=True, key="file"),
            sg.FolderBrowse("Browse Folder"),
        ],
        [
            sg.Text("Image:"),
            sg.Input(size=(25,1), enable_events=True, key="-FILE-"),
            sg.FileBrowse("Browse Image", file_types=file_types),
        ],
        [
            sg.Button("Prev"),
            sg.Button("Next")
        ]
    ]
    
    window = sg.Window("Image Viewer", elements, size=(500, 500))
    images = []
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "file":
            images = parse_folder(values["file"])
            if images:
                load_image(images[0], window)
                location = 0
        if event == "-FILE-":
            filename = values["-FILE-"]
            load_image(filename, window)
        if event == "Next" and images:
            if location == len(images) - 1:
                location = 0
            else:
                location += 1
            load_image(images[location], window)
        if event == "Prev" and images:
            if location == 0:
                location = len(images)-1
            else:
                location -= 1
            load_image(images[location], window)
    
    window.close()
    
if __name__ == "__main__":
    main()
    
