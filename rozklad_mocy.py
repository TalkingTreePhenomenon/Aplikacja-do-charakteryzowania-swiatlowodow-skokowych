import matplotlib.pyplot as plt
import scipy
import scipy.special 
import numpy as np
from functions import dynamiczny_import


def rozklad(włókno=None, m=None, Lp=None, Lk=None, Ls=None, promien=None, dok=None,typ = None,promien_dok = None):
    if włókno == None:
        włókno = "WłóknoUniwersalne" 
    if Lk and Ls == None:
        Lk = Lp
        Ls = 0  
    
    import_włókno = dynamiczny_import("fibers_rob", włókno)
    
    rdzen = np.linspace(0.001, promien)
    plaszcz = np.linspace(promien, 3*promien)
    calosc = np.concatenate((rdzen, plaszcz))
    kat = np.linspace(0,2*np.pi)
    
    RS, Theta = np.meshgrid(calosc, kat)
    XS = RS * np.cos(Theta)
    YS = RS * np.sin(Theta)
    


    dziel = typ.split('_')
    nu =  int(dziel[1])
    m_modu = int(dziel[0][2:])

    amp = np.sin(nu * np.pi * calosc) / calosc 
    amp = amp / np.max(amp)  # normalizacja funkcji do maksimum
    amp_s = np.tile(amp, (kat.size, 1))  # Powielanie funkcji wzdłuż kąta
    amp_s = amp_s * np.exp(1j * m_modu * Theta)
    
    
    fig2, ax2 = plt.subplots()

    cf = ax2.contourf(XS, YS, amp_s.real, vmin=-1, vmax=1, cmap='bwr') 
    ax2.set_title(f"Rozkład mocy modu {typ} ")
    ax2.set_xlabel("Odległość od osi rdzenia")
    ax2.set_ylabel("Odległość od osi rdzenia")
    ax2.axis('equal')  
    fig2.colorbar(cf)
    plt.show()
    

             
                
                