import matplotlib.pyplot as plt
import scipy
import scipy.special 
import numpy as np
from znajdywanie_mod import obliczneff
from functions import dynamiczny_import
from functions import mode

def structure(włókno, m, Lp, Lk, Ls, promien, dok,AE = None, AH= None,BE = None, BH= None):
    mody = []
    
    def ustaw_wartosc(mody, licz_L, licz_m, inf, obiekt_modu):
        while len(mody) <= licz_L:
            mody.append([])  

        while len(mody[licz_L]) <= licz_m:
            mody[licz_L].append([])  

        while len(mody[licz_L][licz_m]) <= inf:
            mody[licz_L][licz_m].append([])  

        mody[licz_L][licz_m][inf] = obiekt_modu


    import_włókno = dynamiczny_import("fibers", włókno)
    wspa = []
    wspc = []
    licz_L = 0

    for ilen in np.arange(Lp, Lk, Ls):
        wspa.append(import_włókno(wavelength=ilen, a=promien).n_a)
        wspc.append(import_włókno(wavelength=ilen, a=promien).n_c)
        licz_m = 0

        for im in range(0, m + 1):
            neff = obliczneff(import_włókno(wavelength=ilen, a=promien), im, dok)
            #print(neff)
            inf = 0
            
            if neff is not None:
                for mod in neff:
                    
                    ustaw_wartosc(mody, licz_L, licz_m, inf, mode(ilen, im, mod[0],mod[1])) 
                    inf += 1
                
            licz_m += 1
        licz_L += 1

    return mody, wspa, wspc