from tkinter import *
from tkinter import ttk

def Style_white():
    app.configure(background="White")
    title.configure(foreground="Black", background="White")
    label1.configure(foreground="Black", background="White")
    textbox.configure(foreground="Black", background="White")

def Style_black():
    app.configure(background="Black")
    title.configure(foreground="White", background="Black")
    label1.configure(foreground="White", background="Black")
    textbox.configure(foreground="White", background="Black")

def reset_status():
    label1.config(text='')

def Run():
    label1.config(text='Executando...')
    app.after(1000, reset_status) 

def Clear():
    textbox.delete('1.0', 'end')

def Inject():
    label1.config(text='Injetado...')
    app.after(1000, reset_status)

app = Tk()
app.title('Executor Sus')
app.geometry('700x400')
app.resizable(width=False, height=False)
app.configure(background="Black")

title = ttk.Label(app, text='Executor', foreground='White', background='Black', font=('Arial', 20))
title.place(x=15, y=5)

label1 = ttk.Label(app, text='', foreground='White', background='Black', font=('Arial', 20))
label1.place(x=530, y=5)

textbox = Text(bg='Black', fg='White', font=('Arial'))
textbox.place(x=15, y=55, width=675, height=250)

button1 = ttk.Button(app, text='Run', command=Run)
button1.place(x=400, y=350)

button2 = ttk.Button(app, text='Clear', command=Clear)
button2.place(x=500, y=350)

button3 = ttk.Button(app, text='Inject', command=Inject)
button3.place(x=600, y=350)

style_White = ttk.Button(app, text="Style White", command=Style_white)
style_White.place(x=100,y=350)

style_Black = ttk.Button(app, text="Style Black", command=Style_black)
style_Black.place(x=15,y=350)

app.mainloop()
