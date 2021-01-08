import time
from commands import command_list
from speech import say, listen
import tkinter as tk
from tkinter import filedialog, Text, PhotoImage, Label
import os
import threading

root_window = tk.Tk()
root_window.title('Helpie')
root_window.resizable(0,0)

class Helpie(threading.Thread):
    def __init__(self, label, root):
        self.root = root
        self.label = label
        threading.Thread.__init__(self)
        self.start()
        
    def execute(self, voice_data, root):
        matched = False
        for key in command_list:
            if voice_data in key:
                response = command_list[key](root)
                matched = True
                if len(response) > 0:
                    say(response)
        if not matched:
            say('Sorry, I do not know that one.')
            
    def run(self):
        say('How can I help you?')
        while 1:
            self.label.show_listening()
            voice_data = listen(self.label.show_processing)
            self.execute(voice_data, self.root)
            time.sleep(5)
            

class Icon:
    def __init__(self, frame):
        self.img = PhotoImage(file="resources/listening.png")
        self.icon = Label(frame, image=self.img)
        self.icon.photo = self.img
        self.icon.pack()
    def show_listening(self):
        self.img = PhotoImage(file="resources/listening.png")
        self.icon.configure(image=self.img)
        self.icon.photo = self.img
    def show_processing(self):
        self.img = PhotoImage(file="resources/processing.png")
        self.icon.configure(image=self.img)
        self.icon.photo = self.img

canvas = tk.Canvas(root_window, height=200, width=200, bg='#263D42')
canvas.pack()
frame = tk.Frame(root_window, bg='white')
frame.place(relwidth=0.75, relheight=0.75, relx=.5, rely=.5, anchor='center')
icon = Icon(frame)

helpie = Helpie(icon, root_window)
root_window.mainloop()

