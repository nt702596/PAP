import pandas as pd
import tkinter as Tk
import sympy as sym
import matplotlib.figure 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
                                               NavigationToolbar2TkAgg)

plt.style.use('fivethirtyeight')
sym.init_printing(use_latex = 'mathjax')

#codes = ('an', 'dc', 'nb', 'js', 'vs', 'dt', 'dm', 'di', 'vz', 'mu', 'dr', 'vg', 'nv')
diasfestivos = ('Año Nuevo', 'Aniversario de la Constitución', 'Natalicio Benito Juárez', 'Jueves Santo', 'Viernes Santo', 'Día del trabajo',\
        'Día de la madre', 'Día de la Independencia', 'Día de la Virgen de Zapopan', 'Día de muertos', 'Día de la Revolución', \
        'Día de la Virgen de Guadalupe', 'Navidad')

def eleccion(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
        #code = countrycodes[idx]
        if name == 'Año Nuevo':
            fun1("-01-01")
            
        elif name == 'Aniversario de la Constitución':
            fun1("-02-05")
        
        elif name == 'Natalicio Benito Juárez':
            fun1("-03-21")
        
        elif name == 'Jueves Santo':
            js()
            
        elif name == 'Viernes Santo':
            vs()
        
        elif name == 'Día del trabajo':
            fun1("-05-01")
            
        elif name == 'Día de la madre':
            fun1("-05-10")
            
        elif name == 'Día de la Independencia':
            fun1("-09-16")
        
        elif name == 'Día de la Virgen de Zapopan':
            fun2("-10-12")
        
        elif name == 'Día de muertos':
            fun2("-11-02")
        
        elif name == 'Día de la Revolución':
            fun2("-11-20")
            
        elif name == 'Día de la Virgen de Guadalupe':
            fun2("-12-12")
            
        elif name == 'Navidad':
            fun2("-12-25")
        
        else:
            pass        

def fun1(d):
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(6,6))
    pl = fig.add_subplot(111)
    #a = []
    for i in range(2, 20, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + str(d)
            anio = int("200" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(anio, newyear['MWh'])
            #a.append(float(newyear['MWh']))
            #pl.legend(a, loc="lower left", bbox_to_anchor=(0.5, 0.))
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + str(d)
            anio = int("20" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(anio, newyear['MWh'])
            #a.append(float(newyear['MWh']))
            #pl.legend(a, loc="lower left", bbox_to_anchor=(0.5, 0.))
            i += 1          
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Año')
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def fun2(d):
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(6,6))
    pl = fig.add_subplot(111)
    for i in range(2, 19, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + str(d)
            anio = int("200" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(anio, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + str(d)
            anio = int("20" + str(i))
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(anio, newyear['MWh'])
            i += 1
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Año')
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def JuevesSanto(anno):
    # Constantes mágicas
    M = 24  
    N = 5
    
    #Cálculo de residuos
    a = anno % 19
    b = anno % 4
    c = anno % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7
    
    # Decidir entre los 2 casos:
    if d+e < 10  :
        dia = d+e+22
        mes = "03"
    else:
        dia = d+e-9
        mes = "04"

    # Excepciones especiales (según artí­culo)
    if dia == 26  and mes == "04":
        dia = 19
    if dia == 25 and mes == "04" and d==28 and e == 6 and a >10:
        dia = 18
    
    if dia < 4:
        if dia == 3:
            if mes == "04":
                mes = "03"
                dia = 31            
        elif dia == 2:
            if mes == "04":
                mes = "03"
                dia = 30
        elif dia == 1:
            if mes == "04":
                mes = "03"
                dia = 29
        
    else:
        dia = str(int(dia) - 3)
        if len(dia) < 2:
            dia = "0" + dia
    
    mes = (str(mes))
    if len(mes) < 2:
        mes = "0" + mes
    #"-11-20" 
    return("-{}-{}".format(mes, dia))

def js():
    
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(6,6))
    pl = fig.add_subplot(111)
    for i in range(2, 20, 1):
        if len(str(i)) == 1:
            anio = int("200" + str(i))
            dia = "200" + str(i) + JuevesSanto(anio)
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(anio, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            anio = int("20" + str(i))
            dia = "20" + str(i) + JuevesSanto(anio)
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(anio, newyear['MWh'])
            i += 1
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Año')
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def ViernesSanto(anno):
    # Constantes mágicas
    M = 24  
    N = 5
    
    #Cálculo de residuos
    a = anno % 19
    b = anno % 4
    c = anno % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7
    
    # Decidir entre los 2 casos:
    if d+e < 10  :
        dia = d+e+22
        mes = "03"
    else:
        dia = d+e-9
        mes = "04"

    # Excepciones especiales (según artí­culo)
    if dia == 26  and mes == "04":
        dia = 19
    if dia == 25 and mes == "04" and d==28 and e == 6 and a >10:
        dia = 18
    
    if dia < 3:
        if dia == 2:
            if mes == "04":
                mes = "03"
                dia = 31   
        elif dia == 1:
            if mes == "04":
                mes = "03"
                dia = 30
            
    else:
        dia = str(int(dia) - 2)
        if len(dia) < 2:
            dia = "0" + dia
    
    mes = (str(mes))
    if len(mes) < 2:
        mes = "0" + mes
    #"-11-20" 
    return("-{}-{}".format(mes, dia))

def vs():
    
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(6,6))
    pl = fig.add_subplot(111)
    for i in range(2, 20, 1):
        if len(str(i)) == 1:
            anio = int("200" + str(i))
            dia = "200" + str(i) + ViernesSanto(anio)
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(anio, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            anio = int("20" + str(i))
            dia = "20" + str(i) + ViernesSanto(anio)
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(anio, newyear['MWh'])
            i += 1
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Año')
    pl.set_title(name)
    fig.tight_layout()
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

fr = Tk.Frame(root, borderwidth=5, relief="sunken", width=500, height=500)
fr.grid(column = 0, row = 0)
fr.pack_propagate(0)

fr2 = Tk.Frame(root, borderwidth=5, relief="sunken", width=500, height=500)
fr2.grid(column = 1, row = 0)
fr2.pack_propagate(0)

fr3 = Tk.Frame(root, borderwidth=5, relief="sunken", width=500, height=500)
fr3.grid(column = 2, row = 0)
fr3.pack_propagate(0)

b = Tk.Button(fr2, text="Comportamiento del día en 17 años", font = 'arial, 12', command=eleccion, \
              relief=('solid'))
b.grid(column=1, row=0)
b.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)

b2 = Tk.Button(fr2, text="Comparación con otros días (no programado)", font = 'arial, 12', \
               relief=('solid'))
b2.grid(column=1, row=1)
b2.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)

lbox = Tk.Listbox(fr)
lbox.delete(0, 'end')
for item in diasfestivos:
    lbox.insert('end', item)
lbox.pack(fill=Tk.BOTH, expand=True)

for i in range(0, len(diasfestivos), 2):
    lbox.itemconfigure(i, background='#F6F6F6')
        
for i in range(1, len(diasfestivos), 2):
    lbox.itemconfigure(i, background='#DDDDDD')

root.mainloop()