import re
import tkinter.font as tkFont
from tkinter import *
import pyperclip
import tkinter.messagebox as msgbox
import webbrowser

tk = Tk()
tk.title('Wiki Remover')
tk.geometry('650x500')
tk.resizable(False,False)

titleFont = 'Century 32'
contentFont = tkFont.Font(family='Arial', size=11)


title = Label(tk, text='Wiki Remover',font=titleFont)
title.place(relx=0.0, rely=0, anchor='nw')
title.pack()

content1 = Label(tk, text='Wiki Remover is an application that aims to remove the unnecessary brackets in a wikipedia article',font=contentFont)
content1.place(relx=0.0, rely=0.1, anchor='nw')

def entry():
    INPUT = textArea.get('1.0', 'end-1c')
    print(INPUT)

    pattern = r'\[.*?\]'
    x = re.sub(pattern, "", INPUT)

    pyperclip.copy(x)

    clipboardAlert = msgbox.showinfo('Copied', 'Copied to clipboard')

textArea = Text(width=80,height=10,wrap=WORD)
textArea.pack(expand=YES, fill=BOTH)
textArea.place(relx=0.001, rely=0.2, anchor='nw')
yscrollbar = Scrollbar(tk, orient=VERTICAL, command=textArea.yview)
yscrollbar.pack(side=RIGHT, fill=Y)
#textArea['yscrollcommand'] = yscrollbar.set

submitBut = Button(tk, text="Remove '[]'",font=contentFont, width=15, height=10, command=entry)
submitBut.place(relx=0.01, rely=0.6, anchor='nw')
submitBut.pack

share = Label(tk, text='Share it to others?', font=contentFont)
share.place(relx=0.3, rely=0.65, anchor='nw')
share.pack

def linkBind(link):
    webbrowser.open_new(link)

twitter = Label(tk, text='Twitter', font=contentFont,cursor='hand2',fg='blue')
twitter.place(relx=0.3, rely=0.70, anchor='nw')
twitter.pack
twitter.bind('<Button-1>', lambda e: linkBind('http://twitter.com'))

fb = Label(tk, text='Facebook', font=contentFont,cursor='hand2',fg='blue')
fb.place(relx=0.3, rely=0.75, anchor='nw')
fb.pack
fb.bind('<Button-1>', lambda e: linkBind('http://fb.com'))

ig = Label(tk, text='Instagram', font=contentFont,cursor='hand2',fg='blue')
ig.place(relx=0.3, rely=0.80, anchor='nw')
ig.pack
ig.bind('<Button-1>', lambda e: linkBind('http://instagram.com'))

credits = Label(tk, text='by Apollo', font=('Arial 8 italic'))
credits.place(relx=0.48, rely=0.95, anchor='nw')
credits.pack

mainloop()

