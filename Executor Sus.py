from tkinter import *
from tkinter import ttk

def Opcao():
    opcao = Toplevel()
    opcao.title("Opção")
    opcao.geometry("250x200")
    opcao.resizable(width=False, height=False)
    opcao.configure(background="Black")

    style_White = ttk.Button(opcao, text="Style White", command=Style_white)
    style_White.place(x=10,y=10)

    style_Black = ttk.Button(opcao, text="Style Black", command=Style_black)
    style_Black.place(x=100,y=10)

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

def Janela():
    janela = Toplevel(app)
    janela.title("Scripts")
    janela.geometry("280x300")
    janela.resizable(width=False, height=False)
    janela.configure(background="Black")

    bt1 = ttk.Button(janela, text="Dex Explorer", command=Dex)
    bt1.place(x=10, y=10)

    bt2 = ttk.Button(janela, text="Infinite Yield", command=Yield)
    bt2.place(x=100, y=10)

    bt3 = ttk.Button(janela, text="Fly V3", command=Fly_V3)
    bt3.place(x=190, y=10)

    bt4 = ttk.Button(janela, text="Btools", command=Btools)
    bt4.place(x=10, y=50)

    bt5 = ttk.Button(janela, text="Invisible", command=Invesible)
    bt5.place(x=100, y=50)

def Dex():
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', 'loadstring(game:HttpGet("https://obj.wearedevs.net/2/scripts/Dex%20Explorer.lua"))()')

def Yield():
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', 'loadstring(game:HttpGet("https://obj.wearedevs.net/2/scripts/Infinite%20Yield.lua"))()')

def Fly_V3():
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', 'loadstring(game:HttpGet("https://raw.githubusercontent.com/XNEOFF/FlyGuiV3/main/FlyGuiV3.txt"))()')

def Btools():
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', 'loadstring(game:HttpGet("https://obj.wearedevs.net/2/scripts/BTools.lua"))()')

def Invesible():
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', 'loadstring(game:HttpGet("https://obj.wearedevs.net/2/scripts/Invisible%20Character.lua"))()')

current_language = "en"

def pt_Br():
    global current_language
    current_language = "pt"
    button1.configure(text="Executar")
    button2.configure(text="Limpar")
    button3.configure(text="Injetar")
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', 'print("Olá, Mundo")')
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
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', 'print("Hello, World!")')
    style_Black.configure(text="Style Black")
    style_White.configure(text="Style White")
    pt_BR.configure(text="Portuguese")
    en.configure(text="English")
    label1.config(text='')

def reset_status():
    label1.config(text='')

def Run():
    if current_language == "pt":
        label1.config(text='Executado...')
    else:
        label1.config(text='Executed...')
    app.after(5000, reset_status) 

def Clear():
    textbox.delete('1.0', 'end')

def Inject():

    if current_language == "pt":
        label1.config(text='Injetado...')
    else:
        label1.config(text='Injected...')
    app.after(5000, reset_status)

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
textbox.insert('1.0', 'print("Hello, World!")')

button1 = ttk.Button(app, text='Run', command=Run)
button1.place(x=400, y=350)

button2 = ttk.Button(app, text='Clear', command=Clear)
button2.place(x=500, y=350)

button3 = ttk.Button(app, text='Inject', command=Inject)
button3.place(x=600, y=350)

style_White = ttk.Button(app, text="Style White", command=Style_white)
style_White.place(x=0,y=999)

style_Black = ttk.Button(app, text="Style Black", command=Style_black)
style_Black.place(x=0,y=999)

pt_BR = ttk.Button(app, text="Portuguese", command=pt_Br)
pt_BR.place(x=15,y=320)

en = ttk.Button(app, text="English", command=En)
en.place(x=100,y=320)

bt_script = ttk.Button(app, text="Scripts", command=Janela)
bt_script.place(x=100,y=350)

bt_op = ttk.Button(app, text="Opção", command=Opcao)
bt_op.place(x=15,y=350)

app.mainloop()
