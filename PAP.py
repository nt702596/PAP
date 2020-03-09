import pandas as pd
import tkinter as Tk
#import sympy as sym
import matplotlib.figure 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
                                               NavigationToolbar2TkAgg)
from PIL import ImageTk, Image
#plt.style.use('tableau-colorblind10')
#sym.init_printing(use_latex = 'mathjax')

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
            l = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', \
                 '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
            bar([1, 1], l)
            
        elif name == 'Aniversario de la Constitución':
            l = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', \
                 '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
            bar([2, 5], l)
        
        elif name == 'Natalicio Benito Juárez':
            l = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', \
                 '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
            bar([3, 21], l)
        
        elif name == 'Jueves Santo':
            a = []
            for i in range(2002, 2020, 1):
                a.append(JuevesSanto(i))
            flat_list = []
            for sublist in a:
                for item in sublist:
                    flat_list.append(item)
            l = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', \
                 '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
            bar(flat_list, l)
        elif name == 'Viernes Santo':
            a = []
            for i in range(2002, 2020, 1):
                a.append(ViernesSanto(i))
            flat_list = []
            for sublist in a:
                for item in sublist:
                    flat_list.append(item)
            l = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', \
                 '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
            bar(flat_list, l)
        
        elif name == 'Día del trabajo':
            l = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', \
                 '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
            bar([5, 1], l)
            
        elif name == 'Día de la madre':
            l = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', \
                 '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
            bar([5, 10], l)
        elif name == 'Día de la Independencia':
            l = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', \
                 '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
            bar2([9, 16], l)
        
        elif name == 'Día de la Virgen de Zapopan':
            l = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', \
                 '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
            bar2([10, 12], l)
        
        elif name == 'Día de muertos':
            l = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', \
                 '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
            bar2([11, 2], l)
        
        elif name == 'Día de la Revolución':
            l = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', \
                 '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
            bar2([11, 20], l)
            
        elif name == 'Día de la Virgen de Guadalupe':
            l = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', \
                 '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
            bar2([12, 12], l)
            
        elif name == 'Navidad':
            l = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', \
                 '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
            bar2([12, 25], l)
        
        else:
            pass        


def Sabadoanterior(anno):
    # Constantes mÃ¡gicas
    M = 24  
    N = 5
    
    #CÃ¡lculo de residuos
    a = anno % 19
    b = anno % 4
    c = anno % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7
    
    # Decidir entre los 2 casos:
    if d+e < 10  :
        dia = d+e+22
        mes = 3
    else:
        dia = d+e-9
        mes = 4

    # Excepciones especiales (segÃºn artÃ­Â­culo)
    if dia == 26  and mes == 4:
        dia = 19
    if dia == 25 and mes == 4 and d==28 and e == 6 and a >10:
        dia = 18
    
    if dia < 9:
        if dia == 8:
            if mes == 4:
                mes = 3
                dia = 31
        if dia == 7:
            if mes == 4:
                mes = 3
                dia = 30
        if dia == 6:
            if mes == 4:
                mes = 3
                dia = 29
        elif dia == 5:
            if mes == 4:
                mes = 3
                dia = 28            
        elif dia == 4:
            if mes == 4:
                mes = 3
                dia = 27
        elif dia == 3:
            if mes == 4:
                mes = 3
                dia = 26
        if dia == 2:
            if mes == 4:
                mes = 3
                dia = 25
        if dia == 1:
            if mes == 4:
                mes = 3
                dia = 24
        
    else:
        dia = (dia - 8)
            
    return(mes, dia)
    
def Domingoanterior(anno):
    # Constantes mÃ¡gicas
    M = 24  
    N = 5
    
    #CÃ¡lculo de residuos
    a = anno % 19
    b = anno % 4
    c = anno % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7
    
    # Decidir entre los 2 casos:
    if d+e < 10  :
        dia = d+e+22
        mes = 3
    else:
        dia = d+e-9
        mes = 4

    # Excepciones especiales (segÃºn artÃ­Â­culo)
    if dia == 26  and mes == 4:
        dia = 19
    if dia == 25 and mes == 4 and d==28 and e == 6 and a >10:
        dia = 18
    
    if dia < 8:
        if dia == 7:
            if mes == 4:
                mes = 3
                dia = 31
        if dia == 6:
            if mes == 4:
                mes = 3
                dia = 30
        if dia == 5:
            if mes == 4:
                mes = 3
                dia = 29
        elif dia == 4:
            if mes == 4:
                mes = 3
                dia = 28            
        elif dia == 3:
            if mes == 4:
                mes = 3
                dia = 27
        elif dia == 2:
            if mes == 4:
                mes = 3
                dia = 26
        if dia == 1:
            if mes == 4:
                mes = 3
                dia = 25
        
    else:
        dia = (dia - 7)
          
    return(mes, dia)

def Lunes(anno):
    # Constantes mÃ¡gicas
    M = 24  
    N = 5
    
    #CÃ¡lculo de residuos
    a = anno % 19
    b = anno % 4
    c = anno % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7
    
    # Decidir entre los 2 casos:
    if d+e < 10  :
        dia = d+e+22
        mes = 3
    else:
        dia = d+e-9
        mes = 4

    # Excepciones especiales (segÃºn artÃ­Â­culo)
    if dia == 26  and mes == 4:
        dia = 19
    if dia == 25 and mes == 4 and d==28 and e == 6 and a >10:
        dia = 18
    
    if dia < 7:
        if dia == 6:
            if mes == 4:
                mes = 3
                dia = 31
        if dia == 5:
            if mes == 4:
                mes = 3
                dia = 30
        elif dia == 4:
            if mes == 4:
                mes = 3
                dia = 29            
        elif dia == 3:
            if mes == 4:
                mes = 3
                dia = 28
        elif dia == 2:
            if mes == 4:
                mes = 3
                dia = 27
        if dia == 1:
            if mes == 4:
                mes = 3
                dia = 26
        
    else:
        dia = (dia - 6)
    
    return(mes, dia)
    
def Martes(anno):
    # Constantes mÃ¡gicas
    M = 24  
    N = 5
    
    #CÃ¡lculo de residuos
    a = anno % 19
    b = anno % 4
    c = anno % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7
    
    # Decidir entre los 2 casos:
    if d+e < 10  :
        dia = d+e+22
        mes = 3
    else:
        dia = d+e-9
        mes = 4

    # Excepciones especiales (segÃºn artÃ­Â­culo)
    if dia == 26  and mes == 4:
        dia = 19
    if dia == 25 and mes == 4 and d==28 and e == 6 and a >10:
        dia = 18
    
    if dia < 6:
        if dia == 5:
            if mes == 4:
                mes = 3
                dia = 31
        if dia == 4:
            if mes == 4:
                mes = 3
                dia = 30
        elif dia == 3:
            if mes == 4:
                mes = 3
                dia = 29            
        elif dia == 2:
            if mes == 4:
                mes = 3
                dia = 28
        elif dia == 1:
            if mes == 4:
                mes = 3
                dia = 27
        
    else:
        dia = (dia - 5)
         
    return(mes, dia)
    
def MiercolesSanto(anno):
    # Constantes mÃ¡gicas
    M = 24  
    N = 5
    
    #CÃ¡lculo de residuos
    a = anno % 19
    b = anno % 4
    c = anno % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7
    
    # Decidir entre los 2 casos:
    if d+e < 10  :
        dia = d+e+22
        mes = 3
    else:
        dia = d+e-9
        mes = 4

    # Excepciones especiales (segÃºn artÃ­Â­culo)
    if dia == 26  and mes == 4:
        dia = 19
    if dia == 25 and mes == 4 and d==28 and e == 6 and a >10:
        dia = 18
    
    if dia < 5:
        if dia == 4:
            if mes == 4:
                mes = 3
                dia = 31
        elif dia == 3:
            if mes == 4:
                mes = 3
                dia = 30            
        elif dia == 2:
            if mes == 4:
                mes = 3
                dia = 29
        elif dia == 1:
            if mes == 4:
                mes = 3
                dia = 28
        
    else:
        dia = (dia - 4)   
        
    return(mes, dia)

def JuevesSanto(anno):
    # Constantes mÃ¡gicas
    M = 24  
    N = 5
    
    #CÃ¡lculo de residuos
    a = anno % 19
    b = anno % 4
    c = anno % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7
    
    # Decidir entre los 2 casos:
    if d+e < 10  :
        dia = d+e+22
        mes = 3
    else:
        dia = d+e-9
        mes = 4

    # Excepciones especiales (segÃºn artÃ­Â­culo)
    if dia == 26  and mes == 4:
        dia = 19
    if dia == 25 and mes == 4 and d==28 and e == 6 and a >10:
        dia = 18
    
    if dia < 4:
        if dia == 3:
            if mes == 4:
                mes = 3
                dia = 31            
        elif dia == 2:
            if mes == 4:
                mes = 3
                dia = 30
        elif dia == 1:
            if mes == 4:
                mes = 3
                dia = 29
        
    else:
        dia = (dia - 3)

    return(mes, dia)

def ViernesSanto(anno):
    # Constantes mÃ¡gicas
    M = 24  
    N = 5
    
    #CÃ¡lculo de residuos
    a = anno % 19
    b = anno % 4
    c = anno % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7
    
    # Decidir entre los 2 casos:
    if d+e < 10  :
        dia = d+e+22
        mes = 3
    else:
        dia = d+e-9
        mes = 4

    # Excepciones especiales (segÃºn artÃ­Â­culo)
    if dia == 26  and mes == 4:
        dia = 19
    if dia == 25 and mes == 4 and d==28 and e == 6 and a >10:
        dia = 18
    
    if dia < 3:
        if dia == 2:
            if mes == 4:
                mes = 3
                dia = 31   
        elif dia == 1:
            if mes == 4:
                mes = 3
                dia = 30
            
    else:
        dia = (dia- 2)
    

    return(mes, dia)

def SabadoSanto(anno):
    # Constantes mÃ¡gicas
    M = 24  
    N = 5
    
    #CÃ¡lculo de residuos
    a = anno % 19
    b = anno % 4
    c = anno % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7
    
    # Decidir entre los 2 casos:
    if d+e < 10  :
        dia = d+e+22
        mes = 3
    else:
        dia = d+e-9
        mes = 4

    # Excepciones especiales (segÃºn artÃ­Â­culo)
    if dia == 26  and mes == 4:
        dia = 19
    if dia == 25 and mes == 4 and d==28 and e == 6 and a >10:
        dia = 18
    
    if dia < 2:
        if dia == 1:
            if mes == 4:
                mes = 3
                dia = 31
        
    else:
        dia = (dia - 1)
        
    return(mes, dia)

def Pascua(anno):
    M = 24  
    N = 5
    
    #CÃ¡lculo de residuos
    a = anno % 19
    b = anno % 4
    c = anno % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7
    
    # Decidir entre los 2 casos:
    if d+e < 10  :
        dia = d+e+22
        mes = 3
    else:
        dia = d+e-9
        mes = 4

    # Excepciones especiales (segÃºn artÃ­culo)
    if dia == 26  and mes == 4:
        dia = 19
    if dia == 25 and mes == 4 and d==28 and e == 6 and a >10:
        dia = 18
    return(mes, dia)

def Lunesposterior(anno):
    M = 24  
    N = 5
    
    #CÃ¡lculo de residuos
    a = anno % 19
    b = anno % 4
    c = anno % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7
    
    # Decidir entre los 2 casos:
    if d+e < 10  :
        dia = d+e+22
        mes = 3
    else:
        dia = d+e-9
        mes = 4 
    
    # Excepciones especiales (segÃºn artÃ­culo)
    if dia == 26  and mes == 4:
        dia = 19
    if dia == 25 and mes == 4 and d==28 and e == 6 and a >10:
        dia = 18
    
    if dia < 32:
        if dia == 31:
            if mes == 3:
                mes = 4
                dia = 1
    else:
        dia += 1
  
    return(mes, dia)
    
    
def Martesposterior(anno):
    M = 24  
    N = 5
    
    #CÃ¡lculo de residuos
    a = anno % 19
    b = anno % 4
    c = anno % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7
    
    # Decidir entre los 2 casos:
    if d+e < 10  :
        dia = d+e+22
        mes = 3
    else:
        dia = d+e-9
        mes = 4 
    
    # Excepciones especiales (segÃºn artÃ­culo)
    if dia == 26  and mes == 4:
        dia = 19
    if dia == 25 and mes == 4 and d==28 and e == 6 and a >10:
        dia = 18
    
    if dia < 32:
        if dia == 31:
            if mes == 3:
                mes = 4
                dia = 2
        if dia == 30:
            if mes == 3:
                mes = 4
                dia = 1
    else:
        dia += 2

  
    return(mes, dia)

def Miercolesposterior(anno):
    M = 24  
    N = 5
    
    #CÃ¡lculo de residuos
    a = anno % 19
    b = anno % 4
    c = anno % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7
    
    # Decidir entre los 2 casos:
    if d+e < 10  :
        dia = d+e+22
        mes = 3
    else:
        dia = d+e-9
        mes = 4 
    
    # Excepciones especiales (segÃºn artÃ­culo)
    if dia == 26  and mes == 4:
        dia = 19
    if dia == 25 and mes == 4 and d==28 and e == 6 and a >10:
        dia = 18
    
    if dia < 32:
        if dia == 31:
            if mes == 3:
                mes = 4
                dia = 3
        if dia == 30:
            if mes == 3:
                mes = 4
                dia = 2
        if dia == 29:
            if mes == 3:
                mes = 4
                dia = 1
    else:
        dia += 3
      
    return(mes, dia)

def cat():
    for widget in fr3.winfo_children():
        widget.destroy()
    load = Image.open("mantenimiento.png")
    load = load.resize((600, 550))
    render = ImageTk.PhotoImage(load)
    img = Tk.Label(fr3, image=render)
    img.image = render
    img.place(x=0, y=0)

def eleccion3(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
        #code = countrycodes[idx]
        if name == 'Año Nuevo':
            boxplot([1, 1, 12, 31, 12, 30, 12, 29, 12, 28, 12, 27, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6], \
                    ["-12-27", "-12-28", "-12-29", "-12-30", "-12-31", "-01-01", "-01-02", "-01-03", \
                       "-01-04", "-01-05", "-01-06"])
            
        elif name == 'Aniversario de la Constitución':
            boxplot([2, 5, 2, 4, 2, 3, 2, 2, 2, 1, 1, 31, 2, 6, 2, 7, 2, 8, 2, 9, 2, 10], \
                    ["-01-31", "-02-01", "-02-02", "-02-03", "-02-04", "-02-05", "-02-06", "-02-07", \
                       "-02-08", "-02-09", "-02-10"])
        
        elif name == 'Natalicio Benito Juárez':
            boxplot([3, 21, 3, 20, 3, 19, 3, 18, 3, 17, 3, 16, 3, 22, 3, 23, 3, 24, 3, 25, 3, 26], \
                    ["-03-16", "-03-17", "-03-18", "-03-19", "-03-20", "-03-21", "-03-22", "-03-23", \
                       "-03-24", "-03-25", "-03-26"])
        
        elif name == 'Jueves Santo':
            lista1 = [] 
            for i in range(2002, 2020, 1):
                lista1.append(JuevesSanto(i))
                    
                lista1.append(Sabadoanterior(i))
                lista1.append(Domingoanterior(i))
                lista1.append(Lunes(i))
                lista1.append(Martes(i))
                lista1.append(MiercolesSanto(i))
                    
                lista1.append(ViernesSanto(i))
                lista1.append(SabadoSanto(i))
                lista1.append(Pascua(i))
                lista1.append(Lunesposterior(i))
                lista1.append(Martesposterior(i))
                    
             
            flat_list = []
            for sublist in lista1:
                for item in sublist:
                    flat_list.append(item)    
            l = ["D", "L", "M", "M", "J", "Viernes Santo", "S", "D", "L", "M", "M"]        
            boxplot(flat_list, l)
            
        elif name == 'Viernes Santo':
            lista1 = [] 
            for i in range(1, 20, 1):
                lista1.append(ViernesSanto(i))
                    
                lista1.append(Domingoanterior(i))
                lista1.append(Lunes(i))
                lista1.append(Martes(i))
                lista1.append(MiercolesSanto(i))
                lista1.append(JuevesSanto(i))
                    
                lista1.append(SabadoSanto(i))
                lista1.append(Pascua(i))
                lista1.append(Lunesposterior(i))
                lista1.append(Martesposterior(i))
                lista1.append(Miercolesposterior(i))
                      

            flat_list = []
            for sublist in lista1:
                for item in sublist:
                    flat_list.append(item)
            l = ["D", "L", "M", "M", "J", "Viernes Santo", "S", "D", "L", "M", "M"]        
            boxplot(flat_list, l)
        
        elif name == 'Día del trabajo':
            boxplot([5, 1, 4, 30, 4, 29, 4, 28, 4, 27, 4, 26, 5, 2, 5, 3, 5, 4, 5, 5, 5, 6], \
                    ["-04-26", "-04-27", "-04-28", "-04-29", "-04-30", "-05-01", "-05-02", "-05-03", \
                       "-05-04", "-05-05", "-05-06"])
            
        elif name == 'Día de la madre':
            boxplot([5, 10, 5, 9, 5, 8, 5, 7, 5, 6, 5, 5, 5, 11, 5, 12, 5, 13, 5, 14, 5, 15], \
                    ["-05-05", "-05-06", "-05-07", "-05-08", "-05-09", "-05-10", "-05-11", "-05-12", \
                       "-05-13", "-05-14", "-05-15"])
            
        elif name == 'Día de la Independencia':
            boxplot([9, 16, 9, 15, 9, 14, 9, 13, 9, 12, 9, 11, 9, 17, 9, 18, 9, 19, 9, 20, 9, 21], \
                    ["-09-11", "-09-12", "-09-13", "-09-14", "-09-15", "-09-16", "-09-17", "-09-18", \
                       "-09-19", "-09-20", "-09-21"])
        
        elif name == 'Día de la Virgen de Zapopan':
            boxplot([10, 12, 10, 11, 10, 10, 10, 9, 10, 8, 10, 7, 10, 13, 10, 14, 10, 15, 10, 16, 10, 17], \
                    ["-10-07", "-10-08", "-10-09", "-10-10", "-10-11", "-10-12", "-10-13", "-10-14", \
                        "-10-15", "-10-16", "-10-17"])
        
        elif name == 'Día de muertos':
            boxplot([11, 2, 11, 1, 10, 31, 10, 30, 10, 29, 10, 28, 11, 3, 11, 4, 11, 5, 11, 6, 11, 7], \
                    ["-10-28", "-10-29", "-10-30", "-10-31", "-11-01", "-11-02", "-11-03", "-11-04", \
                        "-11-05", "-11-06", "-11-07"])
        
        elif name == 'Día de la Revolución':
            boxplot([11, 20, 11, 19, 11, 18, 11, 17, 11, 16, 11, 15, 11, 21, 11, 22, 11, 23, 11, 24, 11, 25], \
                    ["-11-15", "-11-16", "-11-17", "-11-18", "-11-19", "-11-20", "-11-21", "-11-22", \
                        "-11-23", "-11-24", "-11-25"])
            
        elif name == 'Día de la Virgen de Guadalupe':
            boxplot([12, 12, 12, 11, 12, 10, 12, 9, 12, 8, 12, 7, 12, 13, 12, 14, 12, 15, 12, 16, 12, 17], \
                    ["-12-07", "-12-08", "-12-09", "-12-10", "-12-11", "-12-12", "-12-13", "-12-14", \
                        "-12-15", "-12-16", "-12-17"])
            
        elif name == 'Navidad':
            boxplot([12, 25, 12, 24, 12, 23, 12, 22, 12, 21, 12, 20, 12, 26, 12, 27, 12, 28, 12, 29, 12, 30], \
                    ["-12-20", "-12-21", "-12-22", "-12-23", "-12-24", "-12-25", "-12-26", "-12-27", \
                        "-12-28", "-12-29", "-12-30"])
        
        else:
            pass        

def boxplot(a, b):
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(7,7))
    pl = fig.add_subplot(111)
    ny =df2[(df2.index.month == a[0]) & (df2.index.day == a[1])]
    ny_before1 =df2[(df2.index.month == a[2]) & (df2.index.day == a[3])]
    ny_before2 =df2[(df2.index.month == a[4]) & (df2.index.day == a[5])]
    ny_before3 =df2[(df2.index.month == a[6]) & (df2.index.day == a[7])]
    ny_before4 =df2[(df2.index.month == a[8]) & (df2.index.day == a[9])]
    ny_before5 =df2[(df2.index.month == a[10]) & (df2.index.day == a[11])]

    ny_after1 =df2[(df2.index.month == a[12]) & (df2.index.day == a[13])]
    ny_after2 =df2[(df2.index.month == a[14]) & (df2.index.day == a[15])]
    ny_after3 =df2[(df2.index.month == a[16]) & (df2.index.day == a[17])]
    ny_after4 =df2[(df2.index.month == a[18]) & (df2.index.day == a[19])]
    ny_after5 =df2[(df2.index.month == a[20]) & (df2.index.day == a[21])]
    
    #colores = ["lightgray", "lightgray", "lightgray", "lightgray", "lightgray", \
     #          "white", "lightgray", "lightgray", "lightgray", "lightgray", "lightgray"]
    
    boxprops = dict(linestyle='-', linewidth=4, color='k')
    medianprops = dict(linestyle='-', linewidth=5, color='k')
    
    
    pl.boxplot([ny_before5['MWh'], ny_before4['MWh'], ny_before3['MWh'], 
             ny_before2['MWh'], ny_before1['MWh'], ny['MWh'],
             ny_after1['MWh'], ny_after2['MWh'], ny_after3['MWh'], 
             ny_after4['MWh'], ny_after5['MWh']], patch_artist=True, \
                showmeans=True,
                boxprops=boxprops,
                medianprops=medianprops)
    
   
    
    labels = b
    
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Fecha')
    pl.set_xticklabels(labels, rotation = 90)
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def bar(a, b):
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(7,7))
    pl = fig.add_subplot(111)
    etiquetas = []
    for i in range(2002, 2020, 1):
        etiquetas.append(str(i))
        ny = df2[(df2.index.month == a[0]) & (df2.index.day == a[1]) & (df2.index.year == i)]
        pl.bar(str(i), ny['MWh'], color = "dodgerblue")
        
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Fecha')
    pl.set_xticklabels(etiquetas, rotation = 90)
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()

def bar2(a, b):
    for widget in fr3.winfo_children():
        widget.destroy()
    fig = matplotlib.figure.Figure(figsize=(7,7))
    pl = fig.add_subplot(111)
    for i in range(2002, 2019, 1):
        ny = df2[(df2.index.month == a[0]) & (df2.index.day == a[1]) & (df2.index.year == i)]
        pl.bar(str(i), ny['MWh'], color = "dodgerblue")
    labels = b
    
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Fecha')
    pl.set_xticklabels(labels, rotation = 90)
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()
       
df = pd.read_csv("dias_festivos.csv")
df2 = pd.read_excel("datos.xlsx") #leyendo los datos
df2 = df2.set_index("fecha") #establece la fecha como el index
    
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

b = Tk.Button(fr2, text="Comportamiento del día en 17 años", font = 'arial, 12', command=eleccion, \
              relief=('raised'))
b.grid(column=1, row=0)
b.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)

b3 = Tk.Button(fr2, text="Días previos y posteriores en boxplot", font = 'arial, 12', command = eleccion3,\
               relief=('raised'))
b3.grid(column=1, row=1)
b3.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)

b4 = Tk.Button(fr2, text="Pronóstico 1", font = 'arial, 12', command = cat,\
               relief=('raised'))
b4.grid(column=1, row=2)
b4.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)

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