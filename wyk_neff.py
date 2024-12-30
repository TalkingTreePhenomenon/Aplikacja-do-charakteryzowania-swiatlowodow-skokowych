import matplotlib.pyplot as plt
import scipy
import scipy.special 

from functions import dynamiczny_import
import numpy as np
from struktura import structure
import scipy.constants
c = scipy.constants.c


def wykresymody(włókno=None, m=None, Lp=None, Lk=None, Ls=None, promien=None, dok=None):
    if włókno == None:
        włókno = "WłóknoUniwersalne" 
    if Lk and Ls == None:
        Lk = Lp
        Ls = 0  
        
    
        

    Mody, wspa, wspc = structure(włókno, m, Lp, Lk, Ls, promien, dok)
    fale = np.arange(Lp, Lk, Ls)
    
    import_włókno = dynamiczny_import("fibers",włókno)
    info_włokno = import_włókno(wavelength=Lp, a=promien).info
    
    mody_z_grupowane = {}
    

    for ii in range(len(Mody)):
        for jj in range(len(Mody[ii])):
            for kk in range(len(Mody[ii][jj])):
                mod = Mody[ii][jj][kk]
                if mod is not None:  
                    m = mod.m
                    typ = mod.typ
                    if m not in mody_z_grupowane:
                        mody_z_grupowane[m] = {}  
                    if typ not in mody_z_grupowane[m]:
                        mody_z_grupowane[m][typ] = []  
                    mody_z_grupowane[m][typ].append(mod) 
                    # słownik  z  kluczem m i mody tego samego typu jako item
    
    
    
    for m, typy in mody_z_grupowane.items():
        plt.figure()
        
        for typ, mody_typu in typy.items():
            
            wavelengths = [mod.wavelength for mod in mody_typu] 
            refractive_indices = [mod.n for mod in mody_typu]
            
         
            plt.plot(wavelengths, refractive_indices, label=f'Typ={typ}')
        plt.plot(fale,wspa,color = 'black',label=f'Współczynnik załamania rdzenia')  
        plt.plot(fale,wspc,color = 'black',label=f'Współczynnik załamania płaszcza')
        
        plt.title(f'Zależność n$_{{eff}}$ od długości fali dla m={m}\n {info_włokno}')
        plt.xlabel('Długość fali (λ) [μm]')
        plt.ylabel('Efektywny współczynnik załamania')
        plt.grid(True)
        plt.legend(title='Typ modu:', loc='lower left')
        plt.show()
            
            
            
       
            
   
            
            
           