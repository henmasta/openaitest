import os
import json
import random
import openai
from tkinter import *

<<<<<<< HEAD
openai.api_key = "cen"
=======
API = ["cen", 
       "cen", 
       "cen", 
       "cen"
       ]

openai.api_key = random.choice(API)
>>>>>>> d94449d (pyqt5)

question = ''

# GUI
root = Tk()
root.title("GPT-3.5")

WIDTH  = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

BG_GRAY    = "#ABB2B9"
BG_COLOR   = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT      = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

json_file = open('history.json', 'a')
# Send function
def send(self):
     
    send = "You >>> " + e.get()
    txt.insert(END, "\n" + send)

    user = e.get().lower()
    
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user}
            ]
        )
        answer = str(completion.choices[0].message)

        translation = json.loads(answer)
        txt.insert(END, "\n" + "ChatGPT-3.5 >>> " + translation['content'] + '\n')
    
    
        json_file.writelines("\n" + send)
        json_file.writelines("\n" + "ChatGPT-3.5 >>> " + translation['content'] + '\n')
        
        e.delete(0, END)
    except Exception: 
        openai.api_key = random.choice(API) 

root.bind('<Return>', send)

def clear_history():

    txt.delete('1.0', END)
    json_file.close()
    history.close()
    os.remove('history.json')


lable1 = Button(root, bg = BG_COLOR, fg = TEXT_COLOR, text = "Clear history", font = FONT_BOLD, pady = 10, width=20, height=1, command = clear_history).grid(row = 0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width = 60)

txt.grid(row=1, column=0, columnspan=2)
try:
    history = open('history.json', 'r')
    txt.insert(END, "\n" + history.read() + '\n')
except Exception:
    pass


scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg = TEXT_COLOR, font = FONT, width = 55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font = FONT_BOLD, bg = BG_GRAY,
			command = send).grid(row = 2, column = 1)

root.resizable(width = False, height=False)
root.columnconfigure(1, weight=1, minsize=75)
root.rowconfigure(1, weight=1, minsize=50)
root.mainloop()
