import json
from difflib import get_close_matches
from tkinter import Tk, Label, Entry, Button, Text, Scrollbar,Frame

class Chatbot:
    def __init__(self, window):
        window.title('Iris bot')
        window.geometry('400x400')
        window.resizable(0,0)
        self.message_session = Text(window, bd=3, relief="flat", font=("Times", 10), undo=True, wrap="word")
        self.message_session.config(width=45, height=15,bg="#596", fg="white", state='disabled')
        self.overscroll = Scrollbar(window, command=self.message_session.yview)
        self.overscroll.config(width=20)
        self.message_session["yscrollcommand"] = self.overscroll.set
        self.message_position = 1.5
        self.send_button = Button(window, text='send', fg='white', bg='blue',width=9,font=('Times', 12), relief ='flat')
        self.Message_Entry = Entry(window, width=40, font=('Times', 12))
        self.message_session.place(x=20, y=20)
        self.overscroll.place(x=370, y=50)
        self.send_button.place(x=0, y=360)
        self.Message_Entry.place(x=135, y=365)
        self.Brain = json.load(open('knowledge.json'))

root = Tk()
Chatbot(root)
root.mainloop()
