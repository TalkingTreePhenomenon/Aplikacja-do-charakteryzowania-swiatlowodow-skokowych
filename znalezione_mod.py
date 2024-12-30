import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.special 
from functions import dynamiczny_import
from hondrosdebye import znajdzmod
from znajdywanie_mod import obliczneff



def Hondros4(włókno= None,parm= None,L= None,a= None,dok= None): 
    if włókno == None:
        włókno = "WłóknoUniwersalne"

    import_włókno = dynamiczny_import("fibers",włókno)
    info_włokno = import_włókno(wavelength=L, a=a).info
    
  
    pocz = import_włókno(wavelength=L, a=a).n_a
    kon =  import_włókno(wavelength=L, a=a).n_c
  
     
    rootsm = {}
    for im in range(0,parm+1):
            roots = []
            
            neff = znajdzmod(import_włókno(wavelength=L, a=a),im,dok)[0]
            
            if neff is not None:
                for n in neff:
                    roots.append(n)
            rootsm[im] = roots

    if rootsm:
        for rzad,mz in rootsm.items():
            
        
            x_values =  np.arange(pocz+dok, kon-dok, dok)  
            x_values = x_values[::-1]
            y_values =  znajdzmod(import_włókno(wavelength=L, a=a),rzad,dok)[1]
                                                               
            plt.plot(x_values, y_values, label="Funkcja Hondrosa-Debye'a")
            mz_rounded = [round(num, 6) for num in mz]
            plt.scatter(mz, [0]*len(mz) , color='red', label=f"$n_{{eff}}$ modów = {mz_rounded}")
            plt.legend()
            plt.title(f"Funkcja Hondrosa-Debye'a dla m =  {rzad} \n {info_włokno}")
            plt.xlabel(f"$n_{{eff}}$")
            plt.ylabel("HD(n)")
            plt.axhline(0, color='black',linewidth=0.5)
            plt.axvline(0, color='black',linewidth=0.5)
            plt.xlim(pocz-dok,kon+dok)
            plt.ylim(-1,1)
            
            plt.grid(True)
            plt.show()
    else:
        print(f"Funkcja nie ma miejsc zerowych dla m w przedziale 0 do {parm}.")

def Znalezione(włókno= None,parm= None,L= None,a= None,dok= None):
    import_włókno = dynamiczny_import("fibers",włókno)

    rootsm = []
    

    for m in range(0,parm+1):
        nc = import_włókno(wavelength=L, a=a).n_c
        na = import_włókno(wavelength=L, a=a).n_a
        
        mode = obliczneff(import_włókno(wavelength=L, a=a), m, dok)
        
        V = (2*np.pi/L)*a*np.sqrt(nc**2 -na**2)
        
        rootsm.append(mode) 
    return rootsm
            
def czestotliwosc(włókno= None,parm= None,L= None,a= None,dok= None):

    import_włókno = dynamiczny_import("fibers",włókno)

    nc = import_włókno(wavelength=L, a=a).n_c
    na = import_włókno(wavelength=L, a=a).n_a

    
    V = (2*np.pi/L)*a*np.sqrt(nc**2 -na**2)
        
            
    return V        




