import pandas as pd
import tkinter as Tk
import numpy as np
import matplotlib.figure 
import matplotlib.pyplot 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
                                               NavigationToolbar2TkAgg)
import statsmodels.api as sm
from datetime import datetime
from calendar import monthrange

from xlrd.xldate import xldate_as_tuple
from datetime import datetime
#plt.style.use('tableau-colorblind10')
#sym.init_printing(use_latex = 'mathjax')


import matplotlib.pyplot as plt
#from xlrd.xldate import xldate_as_tuple

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf


import warnings

warnings.filterwarnings("ignore")
plt.style.use('default')
from pylab import rcParams

import pandas as pd
import matplotlib.pyplot as plt
#from xlrd.xldate import xldate_as_tuple
import numpy as np
from datetime import datetime
from calendar import monthrange
import scipy as sp
from pandas import Series
from numpy import polynomial
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

from datetime import timedelta

import sklearn
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import statsmodels.api as sm

import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt



#codes = ('an', 'dc', 'nb', 'js', 'vs', 'dt', 'dm', 'di', 'vz', 'mu', 'dr', 'vg', 'nv')
diasfestivos = ('Año Nuevo', 'Aniversario de la Constitución', 'Natalicio Benito Juárez', 'Jueves Santo', 'Viernes Santo', 'Día del trabajo',\
        'Día de la madre', 'Día de la Independencia', 'Día de la Virgen de Zapopan', 'Día de muertos', 'Día de la Revolución', \
        'Día de la Virgen de Guadalupe', 'Navidad')

names = ['año nuevo','aniversario de la Constitución de 1917','natalicio de Benito Juárez Garcia',
        'jueves santo','viernes santo','día del trabajo',
        'día de la madre','día de la Independencia',
        'día de la Virgen de Zapopan','día de los muertos',
        'día de la Revolución','día de la Virgen de Guadalupe',
        'Navidad']

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

def regresion(df):
    
    for widget in fr3.winfo_children():
        widget.destroy()
    
    fr4 = Tk.Frame(fr3, borderwidth=5, relief="sunken", width=600, height=150)
    fr4.grid(column = 0, row = 0)
    fr4.pack_propagate(0)
    
    fr5 = Tk.Frame(fr3, borderwidth=5, relief="sunken", width=600, height=450)
    fr5.grid(column = 0, row = 1)
    fr5.pack_propagate(0)
    
    X = df.iloc[0:14,1:6]
    Y = df.iloc[0:14,0]
    test = np.reshape(X.iloc[-1],5)
    
    X = np.reshape(np.asarray(X), (len(X), 5))
    test_size = 0.20
    n=round(len(X)*(1-test_size))
    X_train = X[0:n,:]
    Y_train = Y[0:n]
    X_test =  X[n:len(X),:]
    Y_test = Y[n:len(X)]
    lr = linear_model.LinearRegression()
    lr.fit(X_train, Y_train)
    Y_pred = lr.predict([X_test[0],X_test[1],X_test[2]])
    
    #print('Coefficients: \n', lr.coef_)
    #print('Intercept: \n', lr.intercept_)
    X = sm.add_constant(X)
    Y_train = list(Y_train)
    temporal = np.asarray(X_train)
    X_train = temporal.tolist() 

    temporal2 = np.asarray(X_test)
    X_test = temporal2.tolist()

    model0 = sm.OLS(Y_train, X_train).fit()
    predictions0 = model0.predict([test]) 
    #print(predictions0)
    
    real = Y[-1]
    error = abs(np.mean((Y_test-Y_pred)/Y_test))
    
    tx1 = "Predicción: " + str(Y_pred)
    label1 = Tk.Label(fr4, text = tx1, font=("arial", 14))
    label1.grid(column = 0, row = 0, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))
    #label1.config(background = "DarkOliveGreen3")
    
    tx2 = "Valores reales: " + str(Y[-1]) + "  " + str(Y[-2]) + "  " + str(Y[-3])
    label2 = Tk.Label(fr4, text = tx2, font=("arial", 14))
    label2.grid(column = 0, row = 1, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))
    #label2.config(background = "DarkOliveGreen3")
    
    tx3 = "MAPE: " + str(error)
    label3 = Tk.Label(fr4, text = tx3, font=("arial", 14))
    label3.grid(column = 0, row = 2, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))
    #label3.config(background = "DarkOliveGreen3")

    fig = matplotlib.figure.Figure(figsize=(4,4))
    pl = fig.add_subplot(111)
    xplot =  np.array([2019,2018,2017])
    yplot = np.array([Y_pred[0], Y_pred[1], Y_pred[2]])
    yplot2 = np.array([Y[-1], Y[-2],Y[-3]])
    
    '''
    j = 1
    for i in range(len(xplot)):
        pl.plot(xplot[i], float(Y_pred[i]), color = "red" )
        pl.plot(xplot[i], float(Y[-j]), color = "blue" )
        j += 1
        '''
    pl.scatter(xplot, yplot, color = "red")
    pl.scatter(xplot, yplot2, color = "blue") 
    pl.plot(xplot, yplot, color = "red")
    pl.plot(xplot, yplot2, color = "blue" )    
    #pl.annotate(str, (xplot , yplot), fontsize='large', fontweight='bold')
    
    pl.legend(["Predicción", "Real"],
               loc=3)
    
    
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Fecha')
    pl.tick_params(labelrotation=45)
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr5)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()
    
    tx1 = "Variables utilizadas para la predicción: Temperatura mínima,\n\
    máxima y promedio, velocidad del viento y consumo del día anterior."
    lb1 = Tk.Label(fr3, text = tx1, font=("arial", 16))
    lb1.grid(column = 0, row = 2, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))
    
def ant_one(mes):
    consumo_ =pd.DataFrame()
    if dates['Conmemoracion'][mes] == names[mes]:
        month= dates.index.month[mes]
        day = dates.index.day[mes]
        nn= monthrange(2002, month)
        n = nn[1]
    if day <=1:
        _day = n
        month = 12
    else: 
        _day = day - 1
    z = list(df2[(df2.index.month == month) & (df2.index.day == _day)]['MWh'])
    consumo_= pd.Series(z)
    return(consumo_)  
    
def eleccion4(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
        #code = countrycodes[idx]
        if name == 'Año Nuevo':
            a_nuevo = fechas_comp[(fechas_comp.Conmemoracion == names[0])].drop(['Conmemoracion','dia sem'], axis =1)
            a_nuevo['Dia ant'] = list(ant_one(0))
            regresion(a_nuevo)
            
        elif name == 'Aniversario de la Constitución':
            a_constitucion = fechas_comp[(fechas_comp.Conmemoracion == names[1])].drop(['Conmemoracion','dia sem'], axis =1)
            a_constitucion['Dia ant'] = list(ant_one(1))
            regresion(a_constitucion)
        
        elif name == 'Natalicio Benito Juárez':
            natalicio_bj = fechas_comp[(fechas_comp.Conmemoracion == names[2])].drop(['Conmemoracion','dia sem'], axis =1)
            natalicio_bj['Dia ant'] = list(ant_one(2))
            regresion(natalicio_bj)
        
        elif name == 'Jueves Santo':
            jueves_santo = fechas_comp[(fechas_comp.Conmemoracion == names[3])].drop(['Conmemoracion','dia sem'], axis =1)
            jueves_santo['Dia ant'] = list(ant_one(3))
            regresion(jueves_santo)
            
        elif name == 'Viernes Santo':
            viernes_santo = fechas_comp[(fechas_comp.Conmemoracion == names[4])].drop(['Conmemoracion','dia sem'], axis =1)
            viernes_santo['Dia ant'] = list(ant_one(3))
            regresion(viernes_santo)
        
        elif name == 'Día del trabajo':
            d_trabajo = fechas_comp[(fechas_comp.Conmemoracion == names[5])].drop(['Conmemoracion','dia sem'], axis =1)
            d_trabajo['Dia ant'] = list(ant_one(4))
            regresion(d_trabajo)
            
        elif name == 'Día de la madre':
            d_madre = fechas_comp[(fechas_comp.Conmemoracion == names[6])].drop(['Conmemoracion','dia sem'], axis =1)
            d_madre['Dia ant'] = list(ant_one(4))
            regresion(d_madre)
            
        elif name == 'Día de la Independencia':
            d_independencia = fechas_comp[(fechas_comp.Conmemoracion == names[7])].drop(['Conmemoracion','dia sem'], axis =1)
            d_independencia.drop(d_independencia.tail(1).index,inplace=True)
            d_independencia['Dia ant'] = list(ant_one(8))
            regresion(d_independencia)
        
        elif name == 'Día de la Virgen de Zapopan':
            Virgen_Zapopan = fechas_comp[(fechas_comp.Conmemoracion == names[8])].drop(['Conmemoracion','dia sem'], axis =1)
            Virgen_Zapopan['Dia ant'] = list(ant_one(9))
            regresion(Virgen_Zapopan)
        
        elif name == 'Día de muertos':
            d_muertos = fechas_comp[(fechas_comp.Conmemoracion == names[9])].drop(['Conmemoracion','dia sem'], axis =1)
            d_muertos['Dia ant'] = list(ant_one(10))
            regresion(d_muertos)
        
        elif name == 'Día de la Revolución':
            d_rev = fechas_comp[(fechas_comp.Conmemoracion == names[10])].drop(['Conmemoracion','dia sem'], axis =1)
            d_rev['Dia ant'] = list(ant_one(10))
            regresion(d_rev)
            
        elif name == 'Día de la Virgen de Guadalupe':
            Virgen_Guadalupe = fechas_comp[(fechas_comp.Conmemoracion == names[11])].drop(['Conmemoracion','dia sem'], axis =1)
            Virgen_Guadalupe['Dia ant'] = list(ant_one(11))
            regresion(Virgen_Guadalupe)
            
        elif name == 'Navidad':
            navidad = fechas_comp[(fechas_comp.Conmemoracion == names[12])].drop(['Conmemoracion','dia sem'], axis =1)
            navidad['Dia ant'] = list(ant_one(11))
            regresion(navidad)
        
        else:
            pass     

def regresion2(df):
    for widget in fr3.winfo_children():
        widget.destroy()
    
    fr4 = Tk.Frame(fr3, borderwidth=5, relief="sunken", width=600, height=150)
    fr4.grid(column = 0, row = 0)
    fr4.pack_propagate(0)
    
    fr5 = Tk.Frame(fr3, borderwidth=5, relief="sunken", width=600, height=450)
    fr5.grid(column = 0, row = 1)
    fr5.pack_propagate(0)
    
    X = df.iloc[0:14,5]
    Y = df.iloc[0:14,0]
    test = np.reshape(X.iloc[-1],1)
    #print(test)
    #print("\n")
    X = np.reshape(np.asarray(X), (len(X), 1))
    test_size = 0.20
    n=round(len(X)*(1-test_size))
    X_train = X[0:n,:]
    Y_train = Y[0:n]
    X_test =  X[n:len(X),:]
    Y_test = Y[n:len(X)]
    lr = linear_model.LinearRegression()
    lr.fit(X_train, Y_train)
    Y_pred = lr.predict([X_test[0],X_test[1],X_test[2]])
    """print('prediccion: ', Y_pred)
    print("\n")
    print('real: ', Y[n:len(Y)])
    print("\n")
    print('Coefficients: \n', lr.coef_)
    print("\n")
    print('Intercept: \n', lr.intercept_)
    print("\n")"""
    X = sm.add_constant(X)
    Y_train = list(Y_train)
    temporal = np.asarray(X_train)
    X_train = temporal.tolist() 

 

    temporal2 = np.asarray(X_test)
    X_test = temporal2.tolist()

    #pred[name]['Regresión lineal 1 var'] = Y_pred[0]

    model0 = sm.OLS(Y_train, X_train).fit()
    predictions0 = model0.predict([X_test]) 
    #print(predictions0)
    #print("\n")
    
    real = Y[-1]
    error = abs(np.mean((Y_test-Y_pred)/Y_test))
    #print("error: ", error)
    #print("\n")
    print_model0 = model0.summary()
    #print(print_model0)
    
    tx1 = "Predicciones: " + str(Y_pred)
    label1 = Tk.Label(fr4, text = tx1, font=("arial", 14))
    label1.grid(column = 0, row = 0, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))
    #label1.config(background = "DarkOliveGreen3")
    
    tx2 = "Valores reales: " + str(Y[-1]) + "  " + str(Y[-2]) + "  " + str(Y[-3])
    label2 = Tk.Label(fr4, text = tx2, font=("arial", 14))
    label2.grid(column = 0, row = 1, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))
    #label2.config(background = "DarkOliveGreen3")
    
    tx3 = "MAPE: " + str(error)
    label3 = Tk.Label(fr4, text = tx3, font=("arial", 14))
    label3.grid(column = 0, row = 2, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))
    #label3.config(background = "DarkOliveGreen3")

    fig = matplotlib.figure.Figure(figsize=(5,5))
    pl = fig.add_subplot(111)
    
    xplot =  np.array([2019,2018,2017])
    yplot = np.array([Y_pred[0], Y_pred[1], Y_pred[2]])
    yplot2 = np.array([Y[-1], Y[-2],Y[-3]])
    
    '''
    j = 1
    for i in range(len(xplot)):
        pl.plot(xplot[i], float(Y_pred[i]), color = "red" )
        pl.plot(xplot[i], float(Y[-j]), color = "blue" )
        j += 1
        '''
    pl.scatter(xplot, yplot, color = "red")
    pl.scatter(xplot, yplot2, color = "blue") 
    pl.plot(xplot, yplot, color = "red")
    pl.plot(xplot, yplot2, color = "blue" )    
    #pl.annotate(str, (xplot , yplot), fontsize='large', fontweight='bold')
    
    pl.legend(["Predicción", "Real"],
               loc=3)
    
    
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Fecha')
    pl.tick_params(labelrotation=45)
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr5)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()
    
    tx1 = "Variable utilizada: día anterior"
    lb1 = Tk.Label(fr3, text = tx1, font=("arial", 16))
    lb1.grid(column = 0, row = 2, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))
    


def eleccion5(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
        #code = countrycodes[idx]
        if name == 'Año Nuevo':
            a_nuevo = fechas_comp[(fechas_comp.Conmemoracion == names[0])].drop(['Conmemoracion','dia sem'], axis =1)
            a_nuevo['Dia ant'] = list(ant_one(0))
            regresion2(a_nuevo)
            
        elif name == 'Aniversario de la Constitución':
            a_constitucion = fechas_comp[(fechas_comp.Conmemoracion == names[1])].drop(['Conmemoracion','dia sem'], axis =1)
            a_constitucion['Dia ant'] = list(ant_one(1))
            regresion2(a_constitucion)
        
        elif name == 'Natalicio Benito Juárez':
            natalicio_bj = fechas_comp[(fechas_comp.Conmemoracion == names[2])].drop(['Conmemoracion','dia sem'], axis =1)
            natalicio_bj['Dia ant'] = list(ant_one(2))
            regresion2(natalicio_bj)
        
        elif name == 'Jueves Santo':
            jueves_santo = fechas_comp[(fechas_comp.Conmemoracion == names[3])].drop(['Conmemoracion','dia sem'], axis =1)
            jueves_santo['Dia ant'] = list(ant_one(3))
            regresion2(jueves_santo)
            
        elif name == 'Viernes Santo':
            viernes_santo = fechas_comp[(fechas_comp.Conmemoracion == names[4])].drop(['Conmemoracion','dia sem'], axis =1)
            viernes_santo['Dia ant'] = list(ant_one(3))
            regresion2(viernes_santo)
        
        elif name == 'Día del trabajo':
            d_trabajo = fechas_comp[(fechas_comp.Conmemoracion == names[5])].drop(['Conmemoracion','dia sem'], axis =1)
            d_trabajo['Dia ant'] = list(ant_one(4))
            regresion2(d_trabajo)
            
        elif name == 'Día de la madre':
            d_madre = fechas_comp[(fechas_comp.Conmemoracion == names[6])].drop(['Conmemoracion','dia sem'], axis =1)
            d_madre['Dia ant'] = list(ant_one(4))
            regresion2(d_madre)
            
        elif name == 'Día de la Independencia':
            d_independencia = fechas_comp[(fechas_comp.Conmemoracion == names[7])].drop(['Conmemoracion','dia sem'], axis =1)
            d_independencia.drop(d_independencia.tail(1).index,inplace=True)
            d_independencia['Dia ant'] = list(ant_one(8))
            regresion2(d_independencia)
        
        elif name == 'Día de la Virgen de Zapopan':
            Virgen_Zapopan = fechas_comp[(fechas_comp.Conmemoracion == names[8])].drop(['Conmemoracion','dia sem'], axis =1)
            Virgen_Zapopan['Dia ant'] = list(ant_one(9))
            regresion2(Virgen_Zapopan)
        
        elif name == 'Día de muertos':
            d_muertos = fechas_comp[(fechas_comp.Conmemoracion == names[9])].drop(['Conmemoracion','dia sem'], axis =1)
            d_muertos['Dia ant'] = list(ant_one(10))
            regresion2(d_muertos)
        
        elif name == 'Día de la Revolución':
            d_rev = fechas_comp[(fechas_comp.Conmemoracion == names[10])].drop(['Conmemoracion','dia sem'], axis =1)
            d_rev['Dia ant'] = list(ant_one(10))
            regresion2(d_rev)
            
        elif name == 'Día de la Virgen de Guadalupe':
            Virgen_Guadalupe = fechas_comp[(fechas_comp.Conmemoracion == names[11])].drop(['Conmemoracion','dia sem'], axis =1)
            Virgen_Guadalupe['Dia ant'] = list(ant_one(11))
            regresion2(Virgen_Guadalupe)
            
        elif name == 'Navidad':
            navidad = fechas_comp[(fechas_comp.Conmemoracion == 'Navidad')].drop(['Conmemoracion','dia sem'], axis =1)
            navidad['Dia ant'] = list(ant_one(11))
            regresion2(navidad)
        
        else:
            pass 

def arima(df2, order):
    for widget in fr3.winfo_children():
                widget.destroy()
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
        
    df = df2['MWh'].astype(float)
    df_log = np.log(df)
    np.array(df_log, dtype=float)
    df_log.dropna(inplace=True)
    #plot_acf(df)
    #plot_pacf(df, method='ols')
    
    df_log_shift = df_log - df_log.shift()
    df_log_shift.dropna(inplace=True)
    #decomposition = seasonal_decompose(df_log) 
    
    model = ARIMA(df_log, order= order)
    results = model.fit()
    #plt.plot(df_log_shift)
    #plt.plot(results.fittedvalues, color='red')
    #plt.title('ARIMA(7,1,1) - Año nuevo')
    
    predictions_ARIMA_diff = pd.Series(results.fittedvalues, copy=True)
    predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
    predictions_ARIMA_log = pd.Series(df_log, index=df_log.index)
    predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum, fill_value=0)
    #predictions_ARIMA = np.exp(predictions_ARIMA_log)
    #plt.plot(df)
    #plt.plot(predictions_ARIMA)
    
    fig = matplotlib.figure.Figure(figsize=(7,7))
    pl = fig.add_subplot(111)
    
    if name == 'Año Nuevo':
        fig = results.plot_predict(1, 20) 
            
    else:
        fig = results.plot_predict(2, 20) 
    
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
        
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Fecha')
    #pl.set_xticklabels(labels, rotation = 0)
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr3)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()   

def eleccion6(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
        #code = countrycodes[idx]
        if name == 'Año Nuevo':
            a_nuevo = fechas_comp[(fechas_comp.Conmemoracion == names[0])].drop(['Conmemoracion','dia sem'], axis =1)
           
            order = (2, 1, 2)
            arima(a_nuevo, order)
            
        elif name == 'Aniversario de la Constitución':
            a_constitucion = fechas_comp[(fechas_comp.Conmemoracion == names[1])].drop(['Conmemoracion','dia sem'], axis =1)
            
            order = (0,2, 1)
            arima(a_constitucion, order)
        
        elif name == 'Natalicio Benito Juárez':
            natalicio_bj = fechas_comp[(fechas_comp.Conmemoracion == names[2])].drop(['Conmemoracion','dia sem'], axis =1)
            
            order=(4,2,0)
            arima(natalicio_bj, (4,2,0))
        
        elif name == 'Jueves Santo':
            jueves_santo = fechas_comp[(fechas_comp.Conmemoracion == names[3])].drop(['Conmemoracion','dia sem'], axis =1)
            
            order=(0,2,1)
            arima(jueves_santo, order)
            
        elif name == 'Viernes Santo':
            viernes_santo = fechas_comp[(fechas_comp.Conmemoracion == names[4])].drop(['Conmemoracion','dia sem'], axis =1)
            
            order=(0,2,1)
            arima(viernes_santo, order)
        
        elif name == 'Día del trabajo':
            d_trabajo = fechas_comp[(fechas_comp.Conmemoracion == names[5])].drop(['Conmemoracion','dia sem'], axis =1)
            
            order = (5,1,0)
            arima(d_trabajo, order)
            
        elif name == 'Día de la madre':
            d_madre = fechas_comp[(fechas_comp.Conmemoracion == names[6])].drop(['Conmemoracion','dia sem'], axis =1)
          
            order = (0,2,1)
            arima(d_madre, order)
            
        elif name == 'Día de la Independencia':
            d_independencia = fechas_comp[(fechas_comp.Conmemoracion == names[7])].drop(['Conmemoracion','dia sem'], axis =1)
           
            order = (3,2,1)
            arima(d_independencia, order)
        
        elif name == 'Día de la Virgen de Zapopan':
            Virgen_Zapopan = fechas_comp[(fechas_comp.Conmemoracion == names[8])].drop(['Conmemoracion','dia sem'], axis =1)
            
            order = (5,2,0)
            arima(Virgen_Zapopan, order)
        
        elif name == 'Día de muertos':
            d_muertos = fechas_comp[(fechas_comp.Conmemoracion == names[9])].drop(['Conmemoracion','dia sem'], axis =1)
            
            order = (5,1,0)
            arima(d_muertos, order)
        
        elif name == 'Día de la Revolución':
            d_rev = fechas_comp[(fechas_comp.Conmemoracion == names[10])].drop(['Conmemoracion','dia sem'], axis =1)
            
            order = (6,2,0)
            arima(d_rev, order)
            
        elif name == 'Día de la Virgen de Guadalupe':
            Virgen_Guadalupe = fechas_comp[(fechas_comp.Conmemoracion == names[11])].drop(['Conmemoracion','dia sem'], axis =1)
           
            order = (1,2,0)
            arima(Virgen_Guadalupe, order)
            
        elif name == 'Navidad':
            navidad = fechas_comp[(fechas_comp.Conmemoracion == names[12])].drop(['Conmemoracion','dia sem'], axis =1)
            
            order = (1,2,0)
            arima(navidad, order)
        
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
    
    
    bxp1 = pl.boxplot([ny_before5['MWh'], ny_before4['MWh'], ny_before3['MWh'], 
             ny_before2['MWh'], ny_before1['MWh'], ny['MWh'],
             ny_after1['MWh'], ny_after2['MWh'], ny_after3['MWh'], 
             ny_after4['MWh'], ny_after5['MWh']],  patch_artist=True,\
                #showmeans=True,
                boxprops=boxprops,
                medianprops=medianprops)
    
    colors = ['lightgray', 'lightgray', 'lightgray', 'lightgray', 'lightgray', \
               'dodgerblue', 'lightgray', 'lightgray', 'lightgray', 'lightgray', 'lightgray']
    for patch, color in zip(bxp1['boxes'], colors):
        patch.set_facecolor(color)
        
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


def regresion_vv_dh(df):
    
    for widget in fr3.winfo_children():
        widget.destroy()
    
    fr4 = Tk.Frame(fr3, borderwidth=5, relief="sunken", width=600, height=100)
    fr4.grid(column = 0, row = 0)
    fr4.pack_propagate(0)
    
    fr5 = Tk.Frame(fr3, borderwidth=5, relief="sunken", width=600, height=450)
    fr5.grid(column = 0, row = 1)
    fr5.pack_propagate(0)
    
    ndat= int(np.round(0.80*len(df)))
    X = df.iloc[:,1:8]
    Y = df.iloc[:,0]
    coef = int(np.round(0.20*len(df)))
    
    Xtrain = X.iloc[0:ndat,:]
    Xtest = X.iloc[ndat:,:]
    Ytrain = Y.iloc[0:ndat]
    Ytest = Y.iloc[ndat:]
    
    lm = linear_model.LinearRegression()
    lm.fit(Xtrain, Ytrain)
    
    Y_pred = lm.predict(Xtest)
    
    error = abs(np.mean((Ytest-Y_pred)/Ytest))
    
    print('Coefficients: \n', lm.coef_)
    print('Intercept: \n', lm.intercept_)

    X = sm.add_constant(X) # agregar una constante
    Ytrain = list(Ytrain)
    temporal= np.asarray(Xtrain)
    Xtrain = temporal.tolist()
    temporal2= np.asarray(Xtest)
    Xtest = temporal2.tolist()
 

    model0 = sm.OLS(Ytrain, Xtrain).fit()
    predictions0 = model0.predict(Xtest) 
    
    #errores[name]['Regresión lineal multivar (MCO)'] = abs(np.mean((Ytest-predictions0)/Ytest))
    
    #pred_lr3[name]= Y_pred[:82]
    #pred_lr4[name]= predictions0[:82]

    print_model0 = model0.summary()
    #print(print_model0)
    
    real = Y[-1]
    error = abs(np.mean((Ytest-Y_pred)/Ytest))
    
    
    tx1 = "Predicciones últimas: " + str(Y_pred[1]) + "  " + str(Y_pred[2]) + "  " + str(Y_pred[3])
    label1 = Tk.Label(fr4, text = tx1, font=("arial", 12))
    label1.grid(column = 0, row = 0, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))
    #label1.config(background = "DarkOliveGreen3")
    
    tx2 = "Valores reales: " + str(Y[-1]) + "  " + str(Y[-2]) + "  " + str(Y[-3])
    label2 = Tk.Label(fr4, text = tx2, font=("arial", 12))
    label2.grid(column = 0, row = 1, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))
    #label2.config(background = "DarkOliveGreen3")
    
    tx3 = "MAPE: " + str(error)
    label3 = Tk.Label(fr4, text = tx3, font=("arial", 12))
    label3.grid(column = 0, row = 2, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))
    #label3.config(background = "DarkOliveGreen3")

    fig = matplotlib.figure.Figure(figsize=(4,4))
    pl = fig.add_subplot(111)
    
    
    
    xplot=[]
    yplot=[]
    yplot2=[]
    for i in range(len(Y_pred)):
        yplot.append(Y_pred[i])
    
    annio = 2019
    for i in range(0, len(Y_pred)):
        xplot.append(annio)
        annio -=1
    
    j = 1
    for i in range(len(xplot)):
        yplot2.append(Y[-j])
        j += 1
        
    xplot=np.array(xplot)
    yplot=np.array(yplot)
    yplot2=np.array(yplot2)
    
    
    pl.scatter(xplot, yplot, color = "red")
    pl.scatter(xplot, yplot2, color = "blue") 
    pl.plot(xplot, yplot, color = "red")
    pl.plot(xplot, yplot2, color = "blue" ) 
    
    pl.legend(["Predicción", "Real"],
               loc=3)
    
    
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Fecha')
    #pl.set_xticklabels(labels, rotation = 0)
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr5)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()
    
    tx1 = "Variables utilizadas para la predicción: Temperatura mínima,\n\
    máxima y promedio, velocidad del viento y consumo del día anterior, consumo 1hr antes,\n\
    consumo 24 hrs antes."
    lb1 = Tk.Label(fr3, text = tx1, font=("arial", 16))
    lb1.grid(column = 0, row = 2, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))


def eleccion7(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
        #code = countrycodes[idx]
        if name == 'Año Nuevo':
            regresion_vv_dh(dia1)
            
        elif name == 'Aniversario de la Constitución':
            regresion_vv_dh(dia2)
        
        elif name == 'Natalicio Benito Juárez':
            regresion_vv_dh(dia3)
        
        elif name == 'Jueves Santo':
            regresion_vv_dh(dia4)
            
        elif name == 'Viernes Santo':
            regresion_vv_dh(dia5)
        
        elif name == 'Día del trabajo':
            regresion_vv_dh(dia6)
            
        elif name == 'Día de la madre':
            regresion_vv_dh(dia7)
            
        elif name == 'Día de la Independencia':
            regresion_vv_dh(dia8)
        
        elif name == 'Día de la Virgen de Zapopan':
            regresion_vv_dh(dia9)
        
        elif name == 'Día de muertos':
            regresion_vv_dh(dia10)
        
        elif name == 'Día de la Revolución':
            regresion_vv_dh(dia11)
            
        elif name == 'Día de la Virgen de Guadalupe':
            regresion_vv_dh(dia12)
            
        elif name == 'Navidad':
            regresion_vv_dh(dia13)
        
        else:
            pass 


def regresion_2v_dh(df):
    
    for widget in fr3.winfo_children():
        widget.destroy()
    
    fr4 = Tk.Frame(fr3, borderwidth=5, relief="sunken", width=600, height=100)
    fr4.grid(column = 0, row = 0)
    fr4.pack_propagate(0)
    
    fr5 = Tk.Frame(fr3, borderwidth=5, relief="sunken", width=600, height=450)
    fr5.grid(column = 0, row = 1)
    fr5.pack_propagate(0)
    
    ndat= int(np.round(0.80*len(df)))
    X = df.iloc[:,1:3]
    Y = df.iloc[:,0]
    
    Xtrain = X.iloc[0:ndat,:]
    Xtest = X.iloc[ndat:,:]
    Ytrain = Y.iloc[0:ndat]
    Ytest = Y.iloc[ndat:]
    
    lm = linear_model.LinearRegression()
    lm.fit(Xtrain, Ytrain)
    
    Y_pred = lm.predict(Xtest)
    
    #errores[name]['Regresión lineal Consumo'] = abs(np.mean((Ytest-Y_pred)/Ytest))
    #pred_lr1[name]=Y_pred[:110]
    
    print('Coefficients: \n', lm.coef_)
    print('Intercept: \n', lm.intercept_)

    X = sm.add_constant(X) # agregar una constante
    Ytrain = list(Ytrain)
    temporal= np.asarray(Xtrain)
    Xtrain = temporal.tolist()
    temporal2= np.asarray(Xtest)
    Xtest = temporal2.tolist()
 

    model0 = sm.OLS(Ytrain, Xtrain).fit()
    predictions0 = model0.predict(Xtest) 
    
    #errores[name]['Regresión lineal Consumo (MCO)'] = abs(np.mean((Ytest-predictions0)/Ytest))
    #pred_lr2[name]= predictions0[:110]

    print_model0 = model0.summary()
    #print(print_model0)
    
    real = Y[-1]
    error = abs(np.mean((Ytest-Y_pred)/Ytest))
    
    
    tx1 = "Predicciones últimas: " + str(Y_pred[1]) + "  " + str(Y_pred[2]) + "  " + str(Y_pred[3])
    label1 = Tk.Label(fr4, text = tx1, font=("arial", 12))
    label1.grid(column = 0, row = 0, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))
    #label1.config(background = "DarkOliveGreen3")
    
    tx2 = "Valores reales: " + str(Y[-1]) + "  " + str(Y[-2]) + "  " + str(Y[-3])
    label2 = Tk.Label(fr4, text = tx2, font=("arial", 12))
    label2.grid(column = 0, row = 1, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))
    #label2.config(background = "DarkOliveGreen3")
    
    tx3 = "MAPE: " + str(error)
    label3 = Tk.Label(fr4, text = tx3, font=("arial", 12))
    label3.grid(column = 0, row = 2, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))
    #label3.config(background = "DarkOliveGreen3")

    fig = matplotlib.figure.Figure(figsize=(4,4))
    pl = fig.add_subplot(111)
    
    xplot=[]
    yplot=[]
    yplot2=[]
    for i in range(len(Y_pred)):
        yplot.append(Y_pred[i])
    
    annio = 2019
    for i in range(0, len(Y_pred)):
        xplot.append(annio)
        annio -=1
    
    j = 1
    for i in range(len(xplot)):
        yplot2.append(Y[-j])
        j += 1
        
    xplot=np.array(xplot)
    yplot=np.array(yplot)
    yplot2=np.array(yplot2)
    
    
    pl.scatter(xplot, yplot, color = "red")
    pl.scatter(xplot, yplot2, color = "blue") 
    pl.plot(xplot, yplot, color = "red")
    pl.plot(xplot, yplot2, color = "blue" ) 
    
    pl.legend(["Predicción", "Real"],
               loc=3)
    
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Fecha')
    #pl.set_xticklabels(labels, rotation = 0)
    pl.set_title(name)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr5)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()
    
    tx1 = "Variables utilizadas para la predicción: consumo 1hr antes,\n\
    consumo 24 hrs antes."
    lb1 = Tk.Label(fr3, text = tx1, font=("arial", 16))
    lb1.grid(column = 0, row = 2, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))



def sarima(a_nuevo):
    
    for widget in fr3.winfo_children():
        widget.destroy()
    
    fr4 = Tk.Frame(fr3, borderwidth=5, relief="sunken", width=600, height=100)
    fr4.grid(column = 0, row = 0)
    fr4.pack_propagate(0)
    
    fr5 = Tk.Frame(fr3, borderwidth=5, relief="sunken", width=600, height=450)
    fr5.grid(column = 0, row = 1)
    fr5.pack_propagate(0)
    
    npa_nuevo = np.array(a_nuevo, dtype=float)
    ndat = np.round(0.80*len(npa_nuevo))
    series = np.log(npa_nuevo)
    
    '''
    plt.plot(series)
    plt.xlabel('Año')
    plt.ylabel('Consumo')
    plt.title('Consumo Horario Año Nuevo')
    plt.show()
    '''
    
    train =a_nuevo[0:int(ndat)]
    test=a_nuevo[int(ndat):len(npa_nuevo)]
    
    #rcParams['figure.figsize'] = 18, 8
    #decomposition = sm.tsa.seasonal_decompose(npa_nuevo, model='additive',
    #                                     freq=24)
    #fig = decomposition.plot()
    #plt.show()
    
    
    p = d = q = range(0, 2)
    pdq = list(itertools.product(p, d, q))
    seasonal_pdq = [(x[0], x[1], x[2], 24) for x in list(itertools.product(p, d, q))]
    
    parameters = pd.DataFrame(columns=['param','param_seasonal','results.aic'])
    
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(np.array(train, dtype=float),order=param,seasonal_order=param_seasonal,enforce_stationarity=False,enforce_invertibility=False)
                results = mod.fit()
                #print('ARIMA{}x{}12 - AIC:{}'.format(param,param_seasonal,results.aic))
            except: 
                continue
    
    #ARIMA(1, 0, 1)x(1, 1, 1, 12)12
    mod_an = sm.tsa.statespace.SARIMAX(np.array(train, dtype=float),
                                order=(1, 0, 1),
                                seasonal_order=(0, 1, 1, 24),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
    results_an = mod_an.fit()
    results_an.summary().tables[1]

    pred_an_1 = results_an.get_prediction(start = int(ndat)+1 , end = len(a_nuevo))
    pred_ci = pred_an_1.conf_int()
    train_an = np.array(a_nuevo, dtype=float)
 
       
    fig = matplotlib.figure.Figure(figsize=(4,4))
    pl = fig.add_subplot(111)
    
    ax= pl.plot(train_an, label='observed')
    pred_an= pd.DataFrame(index= range(int(ndat),len(a_nuevo)),columns=['Forecast'])
    pred_an['Forecast'] = pred_an_1.predicted_mean
    pl.plot(pred_an,color='g', label='One-step ahead Forecast')
    pl.fill_between(pred_an.index,pred_ci[:, 1],
                pred_ci[:, 0], color='k', alpha=.2)
    #plt.xlabel('Time')
    #plt.ylabel('Consumo (MWh)')
    #plt.title('Proyección con modelo SARIMA - Año Nuevo')
    pl.legend()
    #plt.show()
    
    
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
    
    pl.set_ylabel('Consumo en MWh')
    pl.set_xlabel('Tiempo')
    #pl.set_xticklabels(labels, rotation = 0)
    pl.set_title("SARIMA " + str(name))
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=fr5)  
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, fr3)
    toolbar.update()
    canvas.draw()
    
    tx1 = "Variables utilizadas para la predicción: consumo 1hr antes,\n\
    consumo 24 hrs antes."
    lb1 = Tk.Label(fr3, text = tx1, font=("arial", 16))
    lb1.grid(column = 0, row = 2, sticky = (Tk.N, Tk.S, Tk.E, Tk.W))



def eleccion8(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
        #code = countrycodes[idx]
        if name == 'Año Nuevo':
            regresion_2v_dh(dia1)
            
        elif name == 'Aniversario de la Constitución':
            regresion_2v_dh(dia2)
        
        elif name == 'Natalicio Benito Juárez':
            regresion_2v_dh(dia3)
        
        elif name == 'Jueves Santo':
            regresion_2v_dh(dia4)
            
        elif name == 'Viernes Santo':
            regresion_2v_dh(dia5)
        
        elif name == 'Día del trabajo':
            regresion_2v_dh(dia6)
            
        elif name == 'Día de la madre':
            regresion_2v_dh(dia7)
            
        elif name == 'Día de la Independencia':
            regresion_2v_dh(dia8)
        
        elif name == 'Día de la Virgen de Zapopan':
            regresion_2v_dh(dia9)
        
        elif name == 'Día de muertos':
            regresion_2v_dh(dia10)
        
        elif name == 'Día de la Revolución':
            regresion_2v_dh(dia11)
            
        elif name == 'Día de la Virgen de Guadalupe':
            regresion_2v_dh(dia12)
            
        elif name == 'Navidad':
            regresion_2v_dh(dia13)
        
        else:
            pass 


def eleccion10(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
        #code = countrycodes[idx]
        if name == 'Año Nuevo':
            sarima(dia1)
            
        elif name == 'Aniversario de la Constitución':
            sarima(dia2)
        
        elif name == 'Natalicio Benito Juárez':
            sarima(dia3)
        
        elif name == 'Jueves Santo':
            sarima(dia4)
            
        elif name == 'Viernes Santo':
            sarima(dia5)
        
        elif name == 'Día del trabajo':
            sarima(dia6)
            
        elif name == 'Día de la madre':
            sarima(dia7)
            
        elif name == 'Día de la Independencia':
            sarima(dia8)
        
        elif name == 'Día de la Virgen de Zapopan':
            sarima(dia9)
        
        elif name == 'Día de muertos':
            sarima(dia10)
        
        elif name == 'Día de la Revolución':
            sarima(dia11)
            
        elif name == 'Día de la Virgen de Guadalupe':
            sarima(dia12)
            
        elif name == 'Navidad':
            sarima(dia13)
        
        else:
            pass 


def eleccion9(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = diasfestivos[idx]
        #code = countrycodes[idx]
        if name == 'Año Nuevo':
            order = (2, 1, 2)
            arima(dia1, order)
            
        elif name == 'Aniversario de la Constitución':
            order = (0,2, 1)
            arima(dia2, order)
        
        elif name == 'Natalicio Benito Juárez':
            order=(4,2,0)
            arima(dia3, order)
        
        elif name == 'Jueves Santo':
            order=(0,2,1)
            arima(dia4, order)
            
        elif name == 'Viernes Santo':
            order=(0,2,1)
            arima(dia5, order)
        
        elif name == 'Día del trabajo':
            order = (5,1,0)
            arima(dia6, order)
            
        elif name == 'Día de la madre':
            order = (0,2,1)
            arima(dia7, order)
            
        elif name == 'Día de la Independencia':
            order = (3,2,1)
            arima(dia8, order)
        
        elif name == 'Día de la Virgen de Zapopan':
            order = (5,2,0)
            arima(dia9, order)
        
        elif name == 'Día de muertos':
            order = (5,1,0)
            arima(dia10, order)
        
        elif name == 'Día de la Revolución':
            order = (6,2,0)
            arima(dia11, order)
            
        elif name == 'Día de la Virgen de Guadalupe':
            order = (1,2,0)
            arima(dia12, order)
            
        elif name == 'Navidad':
            order = (1,2,0)
            arima(dia13, order)
        
        else:
            pass 

def consumo_1h(df):
    hrs = list(df.index[i] - timedelta(hours=1) for i in range(len(df))) 
    k = dfha1[dfha1.index.isin(hrs)]
    return(k['MWh'].tolist())
    
def consumo_24h(mes):
    consumo_ =pd.DataFrame()
    if dates['Conmemoracion'][mes] == names[mes]:
        month= dates.index[mes].month
        day = dates.index[mes].day
        nn= monthrange(2002, month)
        n = nn[1]
    if day <=1:
        _day = n
        month = 12
    else: 
        _day = day - 1
    z = list(dfha1[(dfha1.index.month == month) & (dfha1.index.day == _day)]['MWh'])
    return(z)    
    
def consumo_1h2(df):
    hrs = list(df.index[i] - timedelta(hours=1) for i in range(len(df))) 
    k = dfha2[dfha2.index.isin(hrs)]
    return(k['MWh'].tolist())
    
def consumo_24h2(mes):
    consumo_ =pd.DataFrame()
    if dates['Conmemoracion'][mes] == names[mes]:
        month= dates.index[mes].month
        day = dates.index[mes].day
        nn= monthrange(2002, month)
        n = nn[1]
    if day <=1:
        _day = n
        month = 12
    else: 
        _day = day - 1
    z = list(dfha2[(dfha2.index.month == month) & (dfha2.index.day == _day)]['MWh'])
    return(z)  

df = pd.read_csv("dias_festivos.csv")
df2 = pd.read_excel("datos.xlsx") #leyendo los datos
df2 = df2.set_index("fecha") #establece la fecha como el index

dates = pd.read_csv("fechas.csv")
dates['Fecha'] = pd.to_datetime(dates['Fecha']) 
dates = dates.set_index("Fecha")

#print(df2)

df2['conmemoracion'] = dates['Conmemoracion']

#print(df2.head())
###

df['fecha_python'] = df['fecha'].apply(lambda x: datetime(*xldate_as_tuple(x, 0)))

comp = pd.read_excel('Consumo GCROC 2002-2019-2.xlsx', 'datos' ,usecols='B:J')
comp.columns = ['MWh', 'Temp min', 'Temp max', 'Temp prom',
               'borrar','borrar1','Vel viento', 'dia sem']
comp =comp.drop(['borrar','borrar1'], axis =1)
comp =comp.drop('fecha',axis = 0)
factor = pd.DataFrame(comp['MWh']/comp['MWh'].shift()).dropna()
factor = factor.join(comp['dia sem'])
s = list(factor.groupby('dia sem'))
fechas_comp = comp.join(dates).dropna()

df_diasfestivos = pd.read_excel("fechas_comp.xls")

#DATOS HORARIOS

def arreglo(dia1, n):
    
    #dia1 = dia1.drop(["Conmemoracion"], axis = 1)
    a24h = list(consumo_24h(n))
    a24h = a24h[:len(a24h)]
    dia1['Consumo -24h'] = a24h
    dia1 = dia1.drop(dia1.index[0])
    #print(dia1.head(5))
    dia1['Consumo -1h'] = consumo_1h(dia1)
    return()

def arreglo2(dia1, n):
    
    #dia1 = dia1.drop(["Conmemoracion"], axis = 1)
    a24h = list(consumo_24h2(n))
    a24h = a24h[:len(a24h)]
    dia1['Consumo -24h'] = a24h
    dia1 = dia1.drop(dia1.index[0])
    #print(dia1.head(5))
    dia1['Consumo -1h'] = consumo_1h2(dia1)
    return()

dfha1 = pd.read_excel("dfha1.xlsx")
dfha2 = pd.read_excel("dfha2.xlsx")

dia1 = pd.read_excel("df1.xlsx")
dia1 = dia1.drop(["Conmemoracion"], axis = 1)
arreglo(dia1, 0)

dia2 = pd.read_excel("df2.xlsx")
dia2 = dia2.drop(["Conmemoracion"], axis = 1)
arreglo(dia2, 1)

dia3 = pd.read_excel("df3.xlsx")
dia3 = dia3.drop(["Conmemoracion"], axis = 1)
arreglo(dia3, 2)

dia4 = pd.read_excel("df4.xlsx")
dia4 = dia4.drop(["Conmemoracion"], axis = 1)
arreglo(dia4, 3)

dia5 = pd.read_excel("df5.xlsx")
dia5 = dia5.drop(["Conmemoracion"], axis = 1)
arreglo(dia5, 3)

dia6 = pd.read_excel("df6.xlsx")
dia6 = dia6.drop(["Conmemoracion"], axis = 1)
arreglo(dia6, 4)

dia7 = pd.read_excel("df7.xlsx")
dia7 = dia7.drop(["Conmemoracion"], axis = 1)
arreglo(dia7, 4)

dia8 = pd.read_excel("df8.xlsx")
dia8 = dia8.drop(["Conmemoracion"], axis = 1)
arreglo2(dia8, 8)

dia9 = pd.read_excel("df9.xlsx")
dia9 = dia9.drop(["Conmemoracion"], axis = 1)
arreglo2(dia9, 9)

dia10 = pd.read_excel("df10.xlsx")
dia10 = dia10.drop(["Conmemoracion"], axis = 1)
arreglo2(dia10, 10)

dia11 = pd.read_excel("df11.xlsx")
dia11 = dia11.drop(["Conmemoracion"], axis = 1)
arreglo2(dia11, 10)

dia12 = pd.read_excel("df12.xlsx")
dia12 = dia12.drop(["Conmemoracion"], axis = 1)
arreglo2(dia12, 11)

dia13 = pd.read_excel("df13.xlsx")
dia13 = dia13.drop(["Conmemoracion"], axis = 1)
arreglo2(dia13, 11)

root = Tk.Tk()
root.title("Consumo de energía en MWh en días festivos")

fr = Tk.Frame(root, borderwidth=5, relief="sunken", width=200, height=600)
fr.grid(column = 0, row = 0)
fr.pack_propagate(0)

fr2 = Tk.Frame(root, borderwidth=5, relief="sunken", width=300, height=600)
fr2.grid(column = 1, row = 0)
fr2.pack_propagate(0)

fr3 = Tk.Frame(root, borderwidth=5, relief="sunken", width=600, height=600)
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

b4 = Tk.Button(fr2, text="Pronóstico varias variables", font = 'arial, 12', command = eleccion4,\
               relief=('raised'))
b4.grid(column=1, row=2)
b4.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)

b5 = Tk.Button(fr2, text="Pronóstico 1 variable", font = 'arial, 12', command = eleccion5,\
               relief=('raised'))
b5.grid(column=1, row=3)
b5.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)

b6 = Tk.Button(fr2, text="ARIMA", font = 'arial, 12', command = eleccion6,\
               relief=('raised'))
b6.grid(column=1, row=4)
b6.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)

b7 = Tk.Button(fr2, text="Regresión 1+ variables, datos horarios", font = 'arial, 12', command = eleccion7,\
               relief=('raised'))
b7.grid(column=1, row=5)
b7.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)



b8 = Tk.Button(fr2, text="Regresión 1 variable, datos horarios", font = 'arial, 12', command = eleccion8,\
               relief=('raised'))
b8.grid(column=1, row=6)
b8.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)

'''
b9 = Tk.Button(fr2, text="ARIMA, datos horarios", font = 'arial, 12', command = eleccion9,\
               relief=('raised'))
b9.grid(column=1, row=6)
b9.pack(fill = Tk.BOTH, padx = 5, pady = 5, expand = 1)
'''



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
