from tkinter import *
from tkinter import ttk

current_language = "en"

def pt_Br():
    global current_language
    current_language = "pt"
    button1.configure(text="Executar")
    button2.configure(text="Limpar")
    button3.configure(text="Injetar")
    style_Black.configure(text="Estilo Preto")
    style_White.configure(text="Estilo Branco")
    pt_BR.configure(text="Português")
    en.configure(text="Inglês")
    label1.config(text='') 

def En():
    global current_language
    current_language = "en"
    button1.configure(text="Run")
    button2.configure(text="Clear")
    button3.configure(text="Inject")
    style_Black.configure(text="Style Black")
    style_White.configure(text="Style White")
    pt_BR.configure(text="Portuguese")
    en.configure(text="English")
    label1.config(text='')

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
    if current_language == "pt":
        label1.config(text='Executado...')
    else:
        label1.config(text='Executed...')
    app.after(1000, reset_status) 

def Clear():
    textbox.delete('1.0', 'end')

def Inject():

    if current_language == "pt":
        label1.config(text='Injetado...')
    else:
        label1.config(text='Injected...')
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

pt_BR = ttk.Button(app, text="Portuguese", command=pt_Br)
pt_BR.place(x=15,y=320)

en = ttk.Button(app, text="English", command=En)
en.place(x=100,y=320)

app.mainloop()
