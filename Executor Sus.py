from tkinter import *
from tkinter import ttk

def Run():
    pass

def Clear():
    textbox.delete('1.0', 'end')

def Inject():
    pass

app = Tk()
app.title('Executor Sus')
app.geometry('700x400')
app.resizable(width=False, height=False)
app.configure(background="Black")

label1 = ttk.Label(app, text='Executor Sus', foreground='White', background='Black', font=('Arial', 20)).place(x=15, y=5)

textbox = Text(bg='Black', fg='White', font=('Arial'))
textbox.place(x=15, y=55, width=675, height=250)

button1 = ttk.Button(app, text='Run', command=Run)
button1.place(x=400, y=350)

button2 = ttk.Button(app, text='Clear', command=Clear)
button2.place(x=500, y=350)

button3 = ttk.Button(app, text='Inject', command=Inject)
button3.place(x=600, y=350)

app.mainloop()
