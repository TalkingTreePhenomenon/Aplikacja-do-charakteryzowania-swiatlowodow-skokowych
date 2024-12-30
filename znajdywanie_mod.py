import numpy as np
import scipy
import scipy.special 
from scipy.optimize import bisect

def obliczneff(fiber, m, dok):
    na = fiber.n_a
    nc = fiber.n_c
    N = np.arange(na+dok, nc-dok, dok)
    L = fiber.wavelength
    a = fiber.a

    def wart_hd(N, m, na, nc, L, a):
        if isinstance(N,float):
            N = np.array([N])
        k = (2*np.pi/L)
        kN = k*N 
        ysi = (( kN ) ** 2 - (k * na) ** 2)
        xsi = ((k * nc) ** 2 - ( kN ) ** 2)
        
        ysi[ysi<0 ] = 0
        xsi[xsi<0 ] = 0
        
        ysi  = np.sqrt(ysi)   
        xsi  = np.sqrt(xsi) 
        
        u = xsi * a
        w = ysi * a
        B = (w ** 2)/ (u ** 2 + w ** 2)
        X = scipy.special.kvp(m, w) / (w * scipy.special.kv(m, w))
        Y = scipy.special.jvp(m, u) / (u * scipy.special.jv(m, u))
        
        return (X + Y) * (na ** 2 * X + nc ** 2 * Y) - ((m * N) / (u** 2 * B )) ** 2

   
   
  
    
    temp = N[::-1]
    dane = wart_hd(temp, m, na, nc, L, a)
    
    miejsca_zerowe = []
    licznik_TE_EH = 1
    licznik_TM_HE = 1
    
    for i in range(0,len(temp)-1):
        
        if dane[i] * dane[i + 1] < 0:
            miejsce_zerowe = bisect(lambda temp: wart_hd(temp, m, na, nc, L, a), temp[i], temp[i + 1])
            
            if m == 0:
                if dane[i] > dane[i + 1]:
                    typ_modu = "TE" 
                    etykieta = f"{typ_modu}{m}_{licznik_TE_EH}"
                    licznik_TE_EH += 1
                elif dane[i] < dane[i + 1]: 
                    typ_modu ="TM"
                    etykieta = f"{typ_modu}{m}_{licznik_TM_HE}"
                    licznik_TM_HE += 1
                
                
            elif m>0:
                if dane[i] > dane[i + 1]:
                    typ_modu ="EH"
                    etykieta = f"{typ_modu}{m}_{licznik_TE_EH}"
                    licznik_TE_EH += 1
                elif dane[i] < dane[i + 1]: 
                    typ_modu ="HE"
                    etykieta = f"{typ_modu}{m}_{licznik_TM_HE}"
                    licznik_TM_HE += 1
               
                
            miejsca_zerowe.append([miejsce_zerowe, etykieta])
           
    
    if miejsca_zerowe:
        return miejsca_zerowe
