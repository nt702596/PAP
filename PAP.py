import pandas as pd
import tkinter as Tk
import sympy as sym
import matplotlib.figure 
import matplotlib.pyplot as plt
<<<<<<< Updated upstream
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
                                               NavigationToolbar2TkAgg)
from PIL import ImageTk, Image
=======
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, 
                                               #NavigationToolbar2TkAgg)
#from PIL import ImageTk, Image
>>>>>>> Stashed changes
plt.style.use('tableau-colorblind10')
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
    fig = matplotlib.figure.Figure(figsize=(7,7))
    pl = fig.add_subplot(111)
    xtick = []
    for i in range(2, 20, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + str(d)
            anio = int("200" + str(i))
            xtick.append(anio)
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(dia, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + str(d)
            anio = int("20" + str(i))
            xtick.append(anio)
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(dia, newyear['MWh'])
            i += 1          
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Año')
    pl.set_xticklabels(xtick, rotation = 90)
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
    fig = matplotlib.figure.Figure(figsize=(7,7))
    pl = fig.add_subplot(111)
    xtick = []
    for i in range(2, 19, 1):
        if len(str(i)) == 1:
            dia = "200" + str(i) + str(d)
            anio = int("200" + str(i))
            xtick.append(anio)
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(dia, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            dia = "20" + str(i) + str(d)
            anio = int("20" + str(i))
            xtick.append(anio)
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(dia, newyear['MWh'])
            i += 1
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Año')
    pl.set_xticklabels(xtick, rotation = 90)
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def MiercolesSanto(anno):
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
    
    if dia < 5:
        if dia == 4:
            if mes == "04":
                mes = "03"
                dia = 31
        elif dia == 3:
            if mes == "04":
                mes = "03"
                dia = 30            
        elif dia == 2:
            if mes == "04":
                mes = "03"
                dia = 29
        elif dia == 1:
            if mes == "04":
                mes = "03"
                dia = 28
        
    else:
        dia = str(int(dia) - 4)
        if len(dia) < 2:
            dia = "0" + dia
    
    mes = (str(mes))
    if len(mes) < 2:
        mes = "0" + mes
        
    return("-{}-{}".format(mes, dia))

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
    fig = matplotlib.figure.Figure(figsize=(7,7))
    pl = fig.add_subplot(111)
    xtick = []
    for i in range(2, 20, 1):
        if len(str(i)) == 1:
            anio = int("200" + str(i))
            dia = "200" + str(i) + JuevesSanto(anio)
            xtick.append(anio)
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(dia, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            anio = int("20" + str(i))
            dia = "20" + str(i) + JuevesSanto(anio)
            xtick.append(anio)
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(dia, newyear['MWh'])
            i += 1
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Año')
    pl.set_xticklabels(xtick, rotation = 90)
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

def SabadoSanto(anno):
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
    
    if dia < 2:
        if dia == 1:
            if mes == "04":
                mes = "03"
                dia = 31
        
    else:
        dia = str(int(dia) - 1)
        if len(dia) < 2:
            dia = "0" + dia
    
    mes = (str(mes))
    if len(mes) < 2:
        mes = "0" + mes
        
    return("-{}-{}".format(mes, dia))

def vs():
    
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(7,7))
    pl = fig.add_subplot(111)
    xtick = []
    for i in range(2, 20, 1):
        if len(str(i)) == 1:
            anio = int("200" + str(i))
            dia = "200" + str(i) + ViernesSanto(anio)
            xtick.append(anio)
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(dia, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            anio = int("20" + str(i))
            dia = "20" + str(i) + ViernesSanto(anio)
            xtick.append(anio)
            newyear = df.query('fecha_python == @dia & dia_semana<=7')
            pl.bar(dia, newyear['MWh'])
            i += 1
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Año')
    pl.set_xticklabels(xtick, rotation = 90)
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def eleccion2(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
        #code = countrycodes[idx]
        if name == 'Año Nuevo':
            comp2dias(["-12-27", "-12-28", "-12-29", "-12-30", "-12-31", "-01-01", "-01-02", "-01-03", \
                       "-01-04", "-01-05", "-01-06"])
            
        elif name == 'Aniversario de la Constitución':
            comp2dias(["-01-31", "-02-01", "-02-02", "-02-03", "-02-04", "-02-05", "-02-06", "-02-07", \
                       "-02-08", "-02-09", "-02-10"])
        
        elif name == 'Natalicio Benito Juárez':
            comp2dias(["-03-16", "-03-17", "-03-18", "-03-19", "-03-20", "-03-21", "-03-22", "-03-23", \
                       "-03-24", "-03-25", "-03-26"])
        
        elif name == 'Jueves Santo':
            d = []
            for i in range(15, 20, 1):
                if len(str(i)) == 1:
                    anio = int("200" + str(i))
                    d.append(str(anio) + MiercolesSanto(anio))
                    d.append(str(anio) + JuevesSanto(anio))
                    d.append(str(anio) + ViernesSanto(anio))
                    i += 1
                elif len(str(i)) == 2:
                    anio = int("20" + str(i))
                    d.append(str(anio) + MiercolesSanto(anio))
                    d.append(str(anio) + JuevesSanto(anio))
                    d.append(str(anio) + ViernesSanto(anio))
                    i += 1
            comp2diasDS(d)        
    
        elif name == 'Viernes Santo':
            d = []
            for i in range(15, 20, 1):
                if len(str(i)) == 1:
                    anio = int("200" + str(i))
                    d.append(str(anio) + JuevesSanto(anio))
                    d.append(str(anio) + ViernesSanto(anio))
                    d.append(str(anio) + SabadoSanto(anio))
                    i += 1
                elif len(str(i)) == 2:
                    anio = int("20" + str(i))
                    d.append(str(anio) + JuevesSanto(anio))
                    d.append(str(anio) + ViernesSanto(anio))
                    d.append(str(anio) + SabadoSanto(anio))
                    i += 1
            comp2diasDS(d)
        
        elif name == 'Día del trabajo':
            comp2dias(["-04-26", "-04-27", "-04-28", "-04-29", "-04-30", "-05-01", "-05-02", "-05-03", \
                       "-05-04", "-05-05", "-05-06"])
            
        elif name == 'Día de la madre':
            comp2dias(["-05-05", "-05-06", "-05-07", "-05-08", "-05-09", "-05-10", "-05-11", "-05-12", \
                       "-05-13", "-05-14", "-05-15"])
            
        elif name == 'Día de la Independencia':
            comp2dias(["-09-11", "-09-12", "-09-13", "-09-14", "-09-15", "-09-16", "-09-17", "-09-18", \
                       "-09-19", "-09-20", "-09-21"])
        
        elif name == 'Día de la Virgen de Zapopan':
            comp2dias2(["-10-07", "-10-08", "-10-09", "-10-10", "-10-11", "-10-12", "-10-13", "-10-14", \
                        "-10-15", "-10-16", "-10-17"])
        
        elif name == 'Día de muertos':
            comp2dias2(["-10-28", "-10-29", "-10-30", "-10-31", "-11-01", "-11-02", "-11-03", "-11-04", \
                        "-11-05", "-11-06", "-11-07"])
        
        elif name == 'Día de la Revolución':
            comp2dias2(["-11-15", "-11-16", "-11-17", "-11-18", "-11-19", "-11-20", "-11-21", "-11-22", \
                        "-11-23", "-11-24", "-11-25"])
            
        elif name == 'Día de la Virgen de Guadalupe':
            comp2dias2(["-12-07", "-12-08", "-12-09", "-12-10", "-12-11", "-12-12", "-12-13", "-12-14", \
                        "-12-15", "-12-16", "-12-17"])
            
        elif name == 'Navidad':
            comp2dias2(["-12-20", "-12-21", "-12-22", "-12-23", "-12-24", "-12-25", "-12-26", "-12-27", \
                        "-12-28", "-12-29", "-12-30"])
        
        else:
            pass  

def comp2dias(d):
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(7,7))
    pl = fig.add_subplot(111)
    xtick = []
    for i in range(15, 20, 1):
        if len(str(i)) == 1:
            for j in range(len(d)):
                if d[j] == "-12-30" or d[j] == "-12-31":
                    dia = "200" + str(i-1) + str(d[j])
                    xtick.append(dia)
                    newyear = df.query('fecha_python == @dia & dia_semana<=7')
                    pl.bar(dia, newyear['MWh'])
                else:
                    dia = "200" + str(i) + str(d[j])
                    xtick.append(dia)
                    newyear = df.query('fecha_python == @dia & dia_semana<=7')
                    pl.bar(dia, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            for j in range(len(d)):
                if d[j] == "-12-30" or d[j] == "-12-31":
                    dia = "20" + str(i-1) + str(d[j])
                    xtick.append(dia)
                    newyear = df.query('fecha_python == @dia & dia_semana<=7')
                    pl.bar(dia, newyear['MWh'])
                else:
                    dia = "20" + str(i) + str(d[j])
                    xtick.append(dia)
                    newyear = df.query('fecha_python == @dia & dia_semana<=7')
                    pl.bar(dia, newyear['MWh'])               
            i += 1          
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Fecha')
    pl.set_xticklabels(xtick, rotation = 90)
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def comp2dias2(d):
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(7,7))
    pl = fig.add_subplot(111)
    xtick = []
    for i in range(15, 19, 1):
        if len(str(i)) == 1:
            for j in range(len(d)):
                dia = "200" + str(i) + str(d[j])
                xtick.append(dia)
                newyear = df.query('fecha_python == @dia & dia_semana<=7')
                pl.bar(dia, newyear['MWh'])
            i += 1
        elif len(str(i)) == 2:
            for j in range(len(d)):
                dia = "20" + str(i) + str(d[j])
                xtick.append(dia)
                newyear = df.query('fecha_python == @dia & dia_semana<=7')
                pl.bar(dia, newyear['MWh'])
            i += 1          
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Fecha')
    pl.set_xticklabels(xtick, rotation = 90)
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def comp2diasDS(d):
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(7,7))
    pl = fig.add_subplot(111)
    xtick = []
    
    for j in d:
        newyear = df.query('fecha_python == @j & dia_semana<=7')
        xtick.append(j)
        pl.bar(j, newyear['MWh'])
                
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Fecha')
    pl.set_xticklabels(xtick, rotation = 90)
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

fr = Tk.Frame(root, borderwidth=5, relief="sunken", width=200, height=550)
fr.grid(column = 0, row = 0)
fr.pack_propagate(0)

fr2 = Tk.Frame(root, borderwidth=5, relief="sunken", width=300, height=550)
fr2.grid(column = 1, row = 0)
fr2.pack_propagate(0)

fr3 = Tk.Frame(root, borderwidth=5, relief="sunken", width=600, height=550)
fr3.grid(column = 2, row = 0)
fr3.pack_propagate(0)


def cat():
    for widget in fr3.winfo_children():
        widget.destroy()
    load = Image.open("cat.jpg")
    render = ImageTk.PhotoImage(load)
    img = Tk.Label(fr3, image=render)
    img.image = render
    img.place(x=0, y=0)


b = Tk.Button(fr2, text="Comportamiento del día en 17 años", font = 'arial, 12', command=eleccion, \
              relief=('raised'))
b.grid(column=1, row=0)
b.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)

b2 = Tk.Button(fr2, text="Comparación con otros días", font = 'arial, 12', command=eleccion2, \
               relief=('raised'))
b2.grid(column=1, row=1)
b2.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)

b3 = Tk.Button(fr2, text="?", font = 'arial, 12', command = cat,\
               relief=('raised'))
b3.grid(column=1, row=2)
b3.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)

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

