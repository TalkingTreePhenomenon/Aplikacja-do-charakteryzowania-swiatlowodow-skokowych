import matplotlib.pyplot as plt
import scipy
import scipy.special 
import numpy as np
from struktura import structure
from functions import dynamiczny_import
c = 299792458 #m/s


def danymod(włókno=None, m=None, Lp=None, Lk=None, Ls=None, promien=None, dok=None,typ = None):
    if włókno == None:
        włókno = "WłóknoUniwersalne" 
    if Lk and Ls == None:
        Lk = Lp
        Ls = 0  
    
    Mody, wspa, wspc = structure(włókno, m, Lp, Lk, Ls, promien, dok)
    fale = np.arange(Lp, Lk, Ls)
  
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
    
    for typ, mody_lista in wybrane_mody.items():
        print(f"Typ: {typ}, Liczba modów: {len(mody_lista)}")
        
        
def stalaprop(włókno=None, m=None, Lp=None, Lk=None, Ls=None, promien=None, dok=None,typ = None):
    if włókno == None:
        włókno = "WłóknoUniwersalne" 
    if Lk and Ls == None:
        Lk = Lp
        Ls = 0  
    
    Mody, wspa, wspc = structure(włókno, m, Lp, Lk, Ls, promien, dok)
    import_włókno = dynamiczny_import("fibers",włókno)
    info_włokno = import_włókno(wavelength=Lp, a=promien).info
    
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
    
    
    for typ, mody in wybrane_mody.items():
        plt.figure(figsize=(14, 6))
        
        wavelengths = []
        B = []
        omega = []
        czestotliwosc =[]
        for mod_typu in mody:
            wavelengths.append(mod_typu.wavelength)  
            
            czestotliwosc.append(c/(mod_typu.wavelength/1000000))
            B.append(mod_typu.n * (2 * np.pi / mod_typu.wavelength))  
            
        
        
        plt.subplot(1, 2, 1)
        plt.plot(wavelengths, B, label=f'Stała propagacji')
        plt.title(f'Zależność stałej propagacji B od λ dla modu {typ}\n{info_włokno}')
        plt.xlabel('Długość fali (λ) [μm]')
        plt.ylabel('Stała propagacji (B)')
        plt.grid(True)
        plt.legend(title='Typ modu:', loc='lower left')
        
       
        
        plt.subplot(1, 2, 2)
        plt.plot(czestotliwosc, B, label=f'Stała propagacji')
        plt.title(f'Zależność stałej propagacji B od ω dla modu {typ}\n{info_włokno}')
        plt.xlabel('Częstotliwość (v) [Hz]')
        plt.ylabel('Stała propagacji (B)')
        plt.grid(True)
        
        plt.legend(title='Typ modu:', loc='lower left')
     
     
        plt.tight_layout()
        plt.show()
        plt.close()
        