
import importlib
import numpy as np
import sympy as sp
import scipy.special 
import scipy.constants

def dynamiczny_import(modul, funkcja):
    
        try:
            modul = importlib.import_module(modul)
            funkcja_do_wyw = getattr(modul, funkcja)
            return funkcja_do_wyw
        except (ModuleNotFoundError, AttributeError) as e:
            print(f"Błąd: {e}")
            return None
            
            
class mode:
        def __init__(self, wavelength, m, n,typ, EZ =None, ER =None ,EO=None ,HZ=None,HR=None ,HO=None):
            self.wavelength = wavelength 
            self.n = n  
            self.m = m  
            self.typ = typ    
            self.EZ= EZ if EZ is not None else [] 
            self.ER= ER if ER is not None else [] 
            self.EO= EO if EO is not None else []
            self.HZ= HZ if HZ is not None else []
            self.HR= HR if HR is not None else []    
            self.HO= HO if HO is not None else []     
             
        

def oblicz_dlardzenia(m,nc, na, a, neff, L,AE,AH):
    
   
    j = 1j 
    omega  = (scipy.constants.c / L) *2*np.pi
    mu0 = 12.566370614 * 10**(-7) #stała magnetycna
    eps  = 1/(mu0*scipy.constants.c**2) #przenikalność próżni
    
   

 
    beta = neff * omega /scipy.constants.c  
    
    xsi =  np.sqrt((2 * np.pi / L) ** 2 * nc ** 2 - (2 * np.pi / L * neff) ** 2)

   
    Jm = scipy.special.jv(m, xsi*a)
    Jm_prime = scipy.special.jvp(m, xsi*a)

    
    Ez = AE * Jm
    Hz = AH * Jm

    Er = -j / xsi**2*( beta * AE * xsi * Jm_prime + j * omega * mu0 * (m / a) * AH * Jm)
    Ephi = -j /xsi**2*(j * beta * AE * (m / a) * Jm - omega * mu0 *xsi * AH * Jm_prime)

    Hr = -j /xsi**2*(beta * AH * xsi * Jm_prime - j * omega * eps * nc ** 2 * (m / a) * AE * Jm)
    Hphi = -j / xsi**2*( j * beta * AH * (m / a) *Jm + omega * eps * nc ** 2* xsi * AE* Jm_prime)

   
    wyniki_rdzen = [Ez, Er, Ephi, Hz, Hr, Hphi]
    
    return wyniki_rdzen     




def oblicz_dlaplaszcza(m,nc, na, a, neff, L,BE,BH):
    
    
    j = 1j  
    omega  = (scipy.constants.c / L) *2*np.pi
    mu0 = 12.566370614 * 10**(-7)
    eps  = 1/(mu0*scipy.constants.c**2)  

   

   
    beta = neff * omega/scipy.constants.c 
    
    ysi = np.sqrt((2*np.pi/L * neff) ** 2 -(2 *np.pi /L)**2 * na **2)
    xsi =  np.sqrt((2 *np.pi/L) **2 * nc** 2 - (2 * np.pi / L*neff) **2)
   
    
    Km = scipy.special.kv(m, ysi*a)
    Km_prime = scipy.special.kvp(m, ysi*a) 

    
    Ez = BE * Km 
    Hz = BH * Km

    Er = j / ysi**2 * ( beta *BE * ysi* Km_prime + j * omega * mu0 * (m / a) * BH * Km)
    Ephi = j /ysi**2 * (j* beta *BE * (m / a) * Km - omega * mu0 * ysi * BH *Km_prime)

    Hr = j / ysi**2 * (beta * BH * ysi * Km_prime - j * omega* eps * na**2* (m / a) * BE * Km)
    Hphi = j / ysi**2 * (j * beta * BH * (m / a) * Km + omega *eps * na**2 * ysi * BE * Km_prime)

    
    wyniki_plaszcz = [Ez, Er, Ephi, Hz, Hr, Hphi]
    
    return wyniki_plaszcz