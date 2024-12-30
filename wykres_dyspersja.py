import matplotlib.pyplot as plt
import scipy
import scipy.special 
from functions import dynamiczny_import
import numpy as np
from struktura import structure
import scipy.constants
c = scipy.constants.c


def dyspersja(włókno=None, m=None, Lp=None, Lk=None, Ls=None, promien=None, dok=None,typ=None):
    if włókno == None:
        włókno = "WłóknoUniwersalne" 
    if Lk and Ls == None:
        Lk = Lp
        Ls = 0  
        
    import_włókno = dynamiczny_import("fibers",włókno)
    info_włokno = import_włókno(wavelength=Lp, a=promien).info
        

    Mody, wspa, wspc = structure(włókno, m, Lp, Lk, Ls, promien, dok)
    fale = np.arange(Lp, Lk, Ls)
    f_dysp = dynamiczny_import("funkcje_dysp", włókno)
    
    wybrane_mody = {}   
    
    for ii in range(len(Mody)):
        for jj in range(len(Mody[ii])):
            for kk in range(len(Mody[ii][jj])):
                mod = Mody[ii][jj][kk]
                if mod is not None:
                    typ_modu = mod.typ
               
                    
                    
                    
                    
                    
                    if typ == "All":
                        if typ_modu in wybrane_mody:
                            wybrane_mody[typ_modu].append(mod)
                        else:
                            wybrane_mody[typ_modu] = [mod]
                        
                    elif typ in ["TE", "EH"] and mod.typ.startswith(typ):
                        if typ_modu in wybrane_mody:
                                wybrane_mody[typ_modu].append(mod)
                        else:
                            wybrane_mody[typ_modu] = [mod] 
                    
                    elif typ in ["TM", "HE"] and mod.typ.startswith(typ):
                        if typ_modu in wybrane_mody:
                                wybrane_mody[typ_modu].append(mod)
                        else:
                            wybrane_mody[typ_modu] = [mod]
                    
                    elif mod.typ == typ:
                        if typ_modu in wybrane_mody:
                                wybrane_mody[typ_modu].append(mod)
                        else:
                            wybrane_mody[typ_modu] = [mod]
                    
                    
    for typ_modu, mody_lista in wybrane_mody.items():
        plt.figure(figsize=(14, 5))
        wavelengths =[]
        dysp = []
        dysp_mod =[]
        
        
        for mod in mody_lista:
            wlokno_dysp = f_dysp()
            wavelengths.append(mod.wavelength)  
            pochodna_mat = wlokno_dysp.core_refractive_index_derivative()
            pochodna_mod = wlokno_dysp.group_refractive_index_derivative()
         
            dysp.append((-mod.wavelength)/c *pochodna_mat.evalf(subs={wlokno_dysp.wavelength: (mod.wavelength)})*10**(12))
            dysp_mod.append(1/c *pochodna_mod.evalf(subs={wlokno_dysp.wavelength: (mod.wavelength)})*10**(12))
            
        
            
        plt.subplot(1, 2, 1)    
        plt.plot(wavelengths, dysp, label=f'Dyspersja materiałowa') 
        
        plt.title(f'Zależność dyspersji materiałowej od długości fali dla modu= {typ_modu}\n {info_włokno}')
        plt.xlabel('Długość fali (λ) [μm]')
        plt.ylabel('Dyspersja $\mathrm{\\frac{ps}{km \cdot nm}}$')
        plt.grid(True)
        plt.legend(loc='lower left')
        
        
        plt.subplot(1, 2, 2)
        plt.plot(wavelengths, dysp_mod, label=f'Dyspersja modowa') 
        
        plt.title(f'Zależność dyspersji modowej od długości fali dla modu= {typ_modu}\n {info_włokno}')
        plt.xlabel('Długość fali (λ) [μm]')
        plt.ylabel('Dyspersja $\mathrm{\\frac{ps}{km \cdot nm}}$')
        plt.grid(True)
        plt.legend(loc='lower left')
        
        
        plt.show()
        plt.close()
            
            
            
           