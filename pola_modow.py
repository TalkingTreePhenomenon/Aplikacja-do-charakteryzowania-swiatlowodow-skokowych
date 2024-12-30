import matplotlib.pyplot as plt
import scipy
import scipy.special 
import numpy as np
from struktura import structure
from functions import oblicz_dlaplaszcza
from functions import oblicz_dlardzenia
from functions import dynamiczny_import


def pola(włókno=None, m=None, Lp=None, Lk=None, Ls=None, promien=None, dok=None,typ = None):
    if włókno == None:
        włókno = "WłóknoUniwersalne" 
    if Lk and Ls == None:
        Lk = Lp
        Ls = 0  

    import_włókno = dynamiczny_import("fibers", włókno)
    info_włokno = import_włókno(wavelength=Lp, a=promien).info
    
    
    
    Mody, wspa, wspc = structure(włókno, m, Lp, Lk, Ls, promien, dok)
    rdzen = np.linspace(0.001, promien)
    plaszcz = np.linspace(promien, 3*promien)
    calosc = np.concatenate((rdzen, plaszcz))
    kat = np.linspace(0,2*np.pi)
    
    RS, Theta = np.meshgrid(calosc, kat)
    XS = RS * np.cos(Theta)
    YS = RS * np.sin(Theta)
    
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
        for mod in mody_lista:
            if mod.wavelength == Lp:
                        
                L = mod.wavelength  
                typ_modu = mod.typ
                dziel = typ.split('_')
                
                nu =  int(dziel[1])
                m_modu   = mod.m
                
                nc = import_włókno(mod.wavelength,promien).n_c
                na = import_włókno(mod.wavelength,promien).n_a
                a = promien
                N = mod.n     

                k = 2 * np.pi / L
                ysi = np.sqrt((k * N) ** 2 - (k) ** 2 * na ** 2)
                xsi = np.sqrt((k) ** 2 * nc ** 2 - (k * N) ** 2)
                u = xsi * a
                w = ysi * a
                km = scipy.special.kv(m_modu, w) 
                jm =  scipy.special.jv(m_modu, u) 
                kmp = scipy.special.kvp(m_modu, w)
                jmp =  scipy.special.jvp(m_modu, u)
                omega  = (scipy.constants.c / L) *2*np.pi
                mu0 = 12.566370614 * 10**(-7) #stała magnetycna
                #eps  = 1/(mu0*scipy.constants.c**2) #przenikalność próżni
                eps = 8.854187817 * 10**(-12)
                beta = N * k
                                
                
                if m_modu == 0:
                    if typ_modu.startswith('TE'):
                        
                        
                        AE = 0
                        AH = 1j 
                        BE = 0
                        BH = jm * AH /km
                        
                        for i in rdzen:
                            dla_rdzenia = oblicz_dlardzenia(m_modu,  nc, na, i, mod.n , mod.wavelength,AE,AH) 
                            mod.EZ.append(dla_rdzenia[0])
                            mod.ER.append(dla_rdzenia[1]) 
                            mod.EO.append(dla_rdzenia[2])
                            mod.HZ.append(dla_rdzenia[3])
                            mod.HR.append(dla_rdzenia[4])
                            mod.HO.append(dla_rdzenia[5])
                            
                            
                        for i in plaszcz:
                            dla_plaszcza =  oblicz_dlaplaszcza(m_modu,  nc, na, i, mod.n , mod.wavelength,BE,BH) 
                            mod.EZ.append(dla_plaszcza[0])
                            mod.ER.append(dla_plaszcza[1]) 
                            mod.EO.append(dla_plaszcza[2])
                            mod.HZ.append(dla_plaszcza[3])
                            mod.HR.append(dla_plaszcza[4])
                            mod.HO.append(dla_plaszcza[5])
                            
                            
                            
                    elif typ_modu.startswith('TM'):
                        AH = 0
                        AE = 1j
                        BH = 0
                        BE = AE * (jm/km)    
                   
                        
                        for i in rdzen:
                            dla_rdzenia = oblicz_dlardzenia(m_modu,  nc, na, i, mod.n , mod.wavelength,AE,AH) 
                            mod.EZ.append(dla_rdzenia[0])
                            mod.ER.append(dla_rdzenia[1]) 
                            mod.EO.append(dla_rdzenia[2])
                            mod.HZ.append(dla_rdzenia[3])
                            mod.HR.append(dla_rdzenia[4])
                            mod.HO.append(dla_rdzenia[5])
                            
                        for i in plaszcz:
                            dla_plaszcza =  oblicz_dlaplaszcza(m_modu,  nc, na, i, mod.n , mod.wavelength,BE,BH) 
                            mod.EZ.append(dla_plaszcza[0])
                            mod.ER.append(dla_plaszcza[1]) 
                            mod.EO.append(dla_plaszcza[2])
                            mod.HZ.append(dla_plaszcza[3])
                            mod.HR.append(dla_plaszcza[4])
                            mod.HO.append(dla_plaszcza[5])
                        
                        
                elif m_modu != 0:   #m rózne od 0
                    
                
                    
                    AE = 1
                    BE =  jm/km *AE
                    AH =  1j/m_modu * (( u ** 2 * ysi**2)/(omega * mu0* (nc ** 2 - na ** 2) * beta)) * (nc ** 2 * (jmp /(u * jm))  + na ** 2 *(kmp/(w * km)))
                    BH = BE * AH
                    
        
                    
                    for i in rdzen:
                        
                        dla_rdzenia = oblicz_dlardzenia(m_modu,  nc, na, i, mod.n , mod.wavelength,AE,AH) 
                        mod.EZ.append(dla_rdzenia[0])
                        mod.ER.append(dla_rdzenia[1]) 
                        mod.EO.append(dla_rdzenia[2])
                        mod.HZ.append(dla_rdzenia[3])
                        mod.HR.append(dla_rdzenia[4])
                        mod.HO.append(dla_rdzenia[5])
                        
                    for i in plaszcz:
                        dla_plaszcza =  oblicz_dlaplaszcza(m_modu,  nc, na, i, mod.n , mod.wavelength,BE,BH) 
                        mod.EZ.append(dla_plaszcza[0])
                        mod.ER.append(dla_plaszcza[1]) 
                        mod.EO.append(dla_plaszcza[2])
                        mod.HZ.append(dla_plaszcza[3])
                        mod.HR.append(dla_plaszcza[4])
                        mod.HO.append(dla_plaszcza[5])
                        


                
                #składowe po promieniu
                
                fig, axes = plt.subplots(2, 3, figsize=(11, 8))
                axes = axes.flatten()
                amplitudes = {
                    "EZ": mod.EZ,
                    "ER": mod.ER,
                    "Etheta": mod.EO,
                    "HZ": mod.HZ,
                    "HR": mod.HR,
                    "Htheta": mod.HO,
                }
                
                for idx, (key, values) in enumerate(amplitudes.items()):
                    ax = axes[idx]

                    
                    real_values = [np.real(v) for v in values]
                    imag_values = [np.imag(v) for v in values]

                    
                    ax.plot(calosc, real_values, label=f"{key} (Re)", color="blue")
                    ax.plot(calosc, imag_values, label=f"{key} (Im)", color="red")
                    
                    
                    ax.set_title(f"{key} od promienia")
                    ax.set_xlabel("Promień [$\mu$m]")
                    ax.set_ylabel(f"Składowa pola {key} ")
                    ax.legend()
                    ax.grid(True)

                
                plt.tight_layout()
                plt.suptitle(f"Mod: {mod.typ}, dla długości fali: {mod.wavelength} $\mu$m \n {info_włokno}", fontsize=16)
                plt.subplots_adjust(top=0.88)
                plt.show()
                
                
                #wykresy składowych 
                fig, axes = plt.subplots(2, 3, figsize=(11, 8))
                axes = axes.flatten()
               
                    
                skladowe = {
                    "EZ": mod.EZ,
                    "ER": mod.ER,
                    "Etheta": mod.EO,
                    "HZ": mod.HZ,
                    "HR": mod.HR,
                    "Htheta": mod.HO,
                }
                
                for idx, (key, values) in enumerate(skladowe.items()):
                 
                    ax = axes[idx]
                    values = np.array([values])
                    Z =  values * np.exp(1j * m_modu * Theta )

            
                    ax = fig.add_subplot(2, 3, idx + 1)
                    colb = ax.contourf(XS, YS, Z.real, cmap='bwr')  #coolwarm bwr seismic RdBu RdBu
                    ax.axis('equal')  
                    fig.colorbar(colb)

                    
                    
                    ax.set_title(f"Rozkład amplitudy {key} ")
                    ax.set_xlabel("Odległość od osi rdzenia")
                    ax.set_ylabel("Odległość od osi rdzenia")


                plt.tight_layout()
                plt.suptitle(f"Mod: {mod.typ}, Długość fali: {mod.wavelength} $\mu$m \n {info_włokno}", fontsize=16)
                plt.subplots_adjust(top=0.88)

                plt.show()
                
                
                #wykres Ex, Ey, Hx, Hy
                fig, axes = plt.subplots(2, 2, figsize=(10, 8))

              
                ax_Ex, ax_Ey, ax_Hx, ax_Hy = axes.flatten()

                
                em = mod.m 
                    
                ER = np.array(mod.ER)  
                ETheta = np.array(mod.EO)
                HR = np.array(mod.HR)
                HTheta = np.array(mod.HO)

                ER_r = ER * np.exp(1j * em * Theta)
                ETheta_r = ETheta * np.exp(1j * em * Theta)
                HR_r = HR * np.exp(1j * em * Theta)
                HTheta_r = HTheta * np.exp(1j * em * Theta)

                Ex = ER_r * np.cos(Theta) - ETheta_r * np.sin(Theta)
                Ey = ER_r * np.sin(Theta) + ETheta_r * np.cos(Theta)
                Hx = HR_r * np.cos(Theta) - HTheta_r * np.sin(Theta)
                Hy = HR_r * np.sin(Theta) + HTheta_r * np.cos(Theta)

                # Wykres Ex
                col1 = ax_Ex.contourf(XS, YS, Ex.real,vmin=np.min(Ex.real), vmax=np.max(Ex.real), cmap='bwr')
                ax_Ex.set_aspect('equal', adjustable='datalim')
                ax_Ex.set_title("Wykres Ex")
                ax_Ex.set_xlabel("X")
                ax_Ex.set_ylabel("Y")
                fig.colorbar(col1)

                # Wykres Ey
                col2 = ax_Ey.contourf(XS, YS, Ey.real,vmin=np.min(Ey.real), vmax=np.max(Ey.real), cmap='bwr')
                ax_Ey.set_aspect('equal', adjustable='datalim')
                ax_Ey.set_title("Wykres Ey")
                ax_Ey.set_xlabel("X")
                ax_Ey.set_ylabel("Y")
                fig.colorbar(col2)
                # Wykres Hx
                col3 =ax_Hx.contourf(XS, YS, Hx.real,vmin=np.min(Hx.real), vmax=np.max(Hx.real), cmap='bwr')
                ax_Hx.set_aspect('equal', adjustable='datalim')
                ax_Hx.set_title("Wykres Hx")
                ax_Hx.set_xlabel("X")
                ax_Hx.set_ylabel("Y")
                fig.colorbar(col3)
                # Wykres Hy
                col4 = ax_Hy.contourf(XS, YS, Hy.real,vmin=np.min(Hy.real), vmax=np.max(Hy.real), cmap='bwr')
                ax_Hy.set_aspect('equal', adjustable='datalim')
                ax_Hy.set_title("Wykres Hy")
                ax_Hy.set_xlabel("X")
                ax_Hy.set_ylabel("Y")
                fig.colorbar(col4)
    
                
                plt.suptitle(f"Mod: {mod.typ}, Długość fali: {mod.wavelength} $\mu$m \n {info_włokno}", fontsize=16)
                plt.tight_layout()
                plt.subplots_adjust(top=0.88)
                plt.show()
        
        
        
        
           