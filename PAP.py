import pandas as pd
import tkinter as Tk
import sympy as sym
import matplotlib.figure 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
                                               NavigationToolbar2TkAgg)

plt.style.use('seaborn-whitegrid')
sym.init_printing(use_latex = 'mathjax')

codes = ('an', 'dc', 'nb', 'js', 'vs', 'dt', 'dm', 'di', 'vz', 'mu', 'dr', 'vg', 'nv')
diasfestivos = ('Año Nuevo', 'Constitución 1917', 'Natalicio Benito Juárez', 'Jueves Santo', 'Viernes Santo', 'Día del trabajo',\
        'Día de la madre', 'Día de la Independencia', 'Virgen de Zapopan', 'Día de muertos', 'Día de la Revolución', \
        'Día de la Virgen de Guadalupe', 'Navidad')

def eleccion(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
        #code = countrycodes[idx]
        if name == 'Año Nuevo':
            an()
        elif name == 'Navidad':
            nv()
        elif name == 'Constitución 1917':
            dc()
        elif name == 'Natalicio Benito Juárez':
            nb()
        elif name == 'Día del trabajo':
            dt()
        elif name == 'Día de la madre':
            dm()
        elif name == 'Día de la Independencia':
            di()
        elif name == 'Virgen de Zapopan':
            vz()
        elif name == 'Día de muertos':
            mu()
        elif name == 'Día de la Revolución':
            dr()
        elif name == 'Día de la Virgen de Guadalupe':
            vg()
        else:
            pass
        
         #Gift sending left as an exercise to the reader
        #sentmsg.set("Sent %s to leader of %s" % (gifts[gift.get()], name))

def an():
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(5,5))
    pl = fig.add_subplot(111)
    for i in range(2, 20, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + "-01-01"
            anio = int("200" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + "-01-01"
            anio = int("20" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1    

    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def dc():
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(5,5))
    pl = fig.add_subplot(111)
    for i in range(2, 20, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + "-02-05"
            anio = int("200" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + "-02-05"
            anio = int("20" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1
    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()
    
def nv():
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(5,5))
    pl = fig.add_subplot(111)
    for i in range(2, 19, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + "-12-25"
            anio = int("200" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + "-12-25"
            anio = int("20" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1    
    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()
            
def nb():
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(5,5))
    pl = fig.add_subplot(111)
    for i in range(2, 20, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + "-03-21"
            anio = int("200" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + "-03-21"
            anio = int("20" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1

    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def dt():
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(5,5))
    pl = fig.add_subplot(111)
    for i in range(2, 20, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + "-05-01"
            anio = int("200" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + "-05-01"
            anio = int("20" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1

    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()
    
def dm():
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(5,5))
    pl = fig.add_subplot(111)
    for i in range(2, 20, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + "-05-10"
            anio = int("200" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + "-05-10"
            anio = int("20" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1

    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()
    
def di():
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(5,5))
    pl = fig.add_subplot(111)
    for i in range(2, 20, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + "-09-16"
            anio = int("200" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + "-09-16"
            anio = int("20" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1

    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def vz():
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(5,5))
    pl = fig.add_subplot(111)
    for i in range(2, 19, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + "-10-12"
            anio = int("200" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + "-10-12"
            anio = int("20" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1

    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def mu():
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(5,5))
    pl = fig.add_subplot(111)
    for i in range(2, 19, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + "-11-02"
            anio = int("200" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + "-11-02"
            anio = int("20" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1

    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def dr():
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(5,5))
    pl = fig.add_subplot(111)
    for i in range(2, 19, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + "-11-20"
            anio = int("200" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + "-11-20"
            anio = int("20" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1

    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def vg():
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(5,5))
    pl = fig.add_subplot(111)
    for i in range(2, 19, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + "-12-12"
            anio = int("200" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + "-12-12"
            anio = int("20" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.scatter(anio, newyear['MWh'])
            i += 1

    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

df = pd.read_csv("dias_festivos.csv")

from xlrd.xldate import xldate_as_tuple
from datetime import datetime

df['fecha_python'] = df['fecha'].apply(lambda x: datetime(*xldate_as_tuple(x, 0)))

root = Tk.Tk()
root.title("Consumo de energía en MWh en días festivos")

fr = Tk.Frame(root, borderwidth=5, relief="sunken", width=400, height=400)
fr.grid(column = 0, row = 0)
fr.pack_propagate(0)

fr2 = Tk.Frame(root, borderwidth=5, relief="sunken", width=400, height=400)
fr2.grid(column = 1, row = 0)
fr2.pack_propagate(0)

fr3 = Tk.Frame(root, borderwidth=5, relief="sunken", width=400, height=400)
fr3.grid(column = 2, row = 0)
fr3.pack_propagate(0)

b = Tk.Button(fr2, text="Comportamiento del día en 17 años", font = 'arial, 12', command=eleccion)
b.grid(column=1, row=0)
b.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)

b2 = Tk.Button(fr2, text="Comparación con otros días", font = 'arial, 12', command=eleccion)
b2.grid(column=1, row=1)
b2.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)

lbox = Tk.Listbox(fr)
lbox.delete(0, 'end')
for item in diasfestivos:
    lbox.insert('end', item)
lbox.pack(fill=Tk.BOTH, expand=True)


root.mainloop()