
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from znalezione_mod import Hondros4
from znalezione_mod import Znalezione
from znalezione_mod  import czestotliwosc
from info_mod import danymod
from wyk_neff import wykresymody
from info_mod import stalaprop
from pola_modow import pola
from wykres_dyspersja import dyspersja
from rozklad_mocy import rozklad
import inspect
import fibers

class MyApp:
    

    
    def __init__(self, root):
        
        self.root = root
        self.root.title("Aplikacja do charakteryzowania światłowodów skokowych")
        self.root.geometry("800x600")
        
        
        
        #wygląd okna
        style = ttk.Style()
        style.theme_use("clam")  # Dostępne: 'default', 'clam', 'alt', 'classic'
        
        root.attributes('-alpha', 0.95)  #widocznosc
        root.config(cursor="arrow") 
        root.config(bg="lightblue")
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(17, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(6, weight=1)


        #parametry
        self.wlokna_var = self.pobierz_wlokna(fibers)
        self.parm_var = tk.StringVar(value="3") 
        self.Lp_var = tk.StringVar(value="1")  
        self.Lk_var = tk.StringVar(value="1.7")
        self.Ls_var = tk.StringVar(value="0.05") 
        self.a_var = tk.StringVar(value="7")
        self.dok_var = tk.StringVar(value="0.0000011")
        self.typ_var = tk.StringVar(value="EH2_1")
        self.promien_dok_var = tk.StringVar(value="50")
        self.kat_dok_var = tk.StringVar(value="50")
        self.dysp_var = tk.StringVar(value="Off")

        #m
        tk.Label(root, text="Podaj parametr m:").grid(row=1, column=2, padx=5, pady=5)
        self.parm_entry = tk.Entry(root,textvariable=self.parm_var)
        self.parm_entry.grid(row=2, column=2, padx=5, pady=5)
        
        #włokno
        tk.Label(root, text="Podaj włókno:").grid(row=3, column=2, padx=5, pady=5)
        self.włókno_entry = ttk.Combobox(root,values=self.wlokna_var)
        self.włókno_entry.grid(row= 4,column=2 ,padx=5,pady=5)
        
    
        
        #długość fali
        tk.Label(root, text="Początek zakresu:").grid(row=5, column=2, padx=5, pady=5)
        tk.Label(root, text="Koniec zakresu:").grid(row=5, column=3, padx=5, pady=5)
        tk.Label(root, text="Podaj krok długości fali:").grid(row=5, column=4, padx=5, pady=5)
        
        self.Lp_entry = tk.Entry(root,textvariable=self.Lp_var)
        self.Lk_entry = tk.Entry(root,textvariable=self.Lk_var)
        self.Ls_entry = tk.Entry(root,textvariable=self.Ls_var)
        
        self.Lp_entry.grid(row=6, column=2, padx=5, pady=5)
        self.Lk_entry.grid(row=6, column=3, padx=5, pady=5)
        self.Ls_entry.grid(row=6, column=4, padx=5, pady=5)
        
        
        #rdzeń
        tk.Label(root, text="Podaj parametr a:").grid(row=7, column=2, padx=5, pady=5)
        self.a_entry = tk.Entry(root,textvariable=self.a_var)
        self.a_entry.grid(row=8, column=2, padx=5, pady=5)
        #krok
        tk.Label(root, text="Podaj krok:").grid(row=9, column=2, padx=5, pady=5)
        self.dok_entry = tk.Entry(root,textvariable=self.dok_var)
        self.dok_entry.grid(row=10, column=2, padx=5, pady=5)
    
        #typ modu
        tk.Label(root, text="Podaj typ modu:").grid(row=11, column=2, padx=5, pady=5)
        self.typ_entry = tk.Entry(root,textvariable=self.typ_var)
        self.typ_entry.grid(row=12, column=2, padx=5, pady=5)
      
      
      
      
        # Przyciski
        self.submit_button3 = tk.Button(root, text="Wykresy HD", command=self.potw_mz)
        self.submit_button3.grid(row=1, column=5, padx=5, pady=5)
         
        self.przyciskwyniki = tk.Button(root, text="Pokaż wyniki", command=self.okno_wynik)
        self.przyciskwyniki.grid(row=11, column=5, padx=5, pady=5)
        
        
        self.przyciskneff = tk.Button(root,text="Wykres neff od λ",command=self.wykresmodybut)
        self.przyciskneff.grid(row=3, column=5, padx=5, pady=5)
        
        
        self.przyciskstalab = tk.Button(root,text="Wykresy stałej propagacji",command=self.wykres_stala_prop_but)
        self.przyciskstalab.grid(row=7, column=5, padx=5, pady=5)
        
        self.przyciskpola = tk.Button(root,text="Rozkład pól w włóknie",command=self.wykres_pola_but)
        self.przyciskpola.grid(row=5, column=5, padx=5, pady=5)
        
        self.przyciskdyspersja = tk.Button(root,text="Wykresy dyspersji",command=self.wykres_dyspersja_but)
        self.przyciskdyspersja.grid(row=9, column=5, padx=5, pady=5)
        
        
        #przyciski informacyjne
        self.info_m = tk.Button(root, text="?", command=self.otworz_informacja_m,width=2, height=1)
        self.info_m.grid(row=2, column=1, padx=5, pady=5)
        
        
        self.info_wlokno = tk.Button(root, text="?", command=self.otworz_informacja_wlokno,width=2, height=1)
        self.info_wlokno.grid(row=4, column=1, padx=5, pady=5)
        
        self.info_lambda = tk.Button(root, text="?", command=self.otworz_informacja_lambda,width=2, height=1)
        self.info_lambda.grid(row=6, column=1, padx=5, pady=5)
        
        
        self.info_promien = tk.Button(root, text="?", command=self.otworz_informacja_promien,width=2, height=1)
        self.info_promien.grid(row=8, column=1, padx=5, pady=5)
        
        self.info_dok = tk.Button(root, text="?", command=self.otworz_informacja_dok,width=2, height=1)
        self.info_dok.grid(row=10, column=1, padx=5, pady=5)
      
      
    
        self.info_typ = tk.Button(root, text="?", command=self.otworz_informacja_typ,width=2, height=1)
        self.info_typ.grid(row=12, column=1, padx=5, pady=5)
        
        
        self.info_wykreszero = tk.Button(root, text="?", command=self.otworz_informacja_wykreszera,width=2, height=1)
        self.info_wykreszero.grid(row=1, column=6, padx=5, pady=5)
        
        self.info_wykrestala = tk.Button(root, text="?", command=self.otworz_informacja_wykresstala,width=2, height=1)
        self.info_wykrestala.grid(row=7, column=6, padx=5, pady=5)
        
        self.info_wykresneff = tk.Button(root, text="?", command=self.otworz_informacja_wykresneff,width=2, height=1)
        self.info_wykresneff.grid(row=3, column=6, padx=5, pady=5)
        
        self.info_wykresamplitudy = tk.Button(root, text="?", command=self.otworz_informacja_wykresamplitudy,width=2, height=1)
        self.info_wykresamplitudy.grid(row=5, column=6, padx=5, pady=5)
        
        self.info_znalezione = tk.Button(root, text="?", command=self.otworz_informacja_znalezione,width=2, height=1)
        self.info_znalezione.grid(row=11, column=6, padx=5, pady=5)
        
        self.info_dysp = tk.Button(root, text="?", command=self.otworz_informacja_dyspersja,width=2, height=1)
        self.info_dysp.grid(row=9, column=6, padx=5, pady=5)
        
        
        
    def wykres_rozklad_but(self):
        parm = int(self.parm_entry.get())
        Lp = float(self.Lp_entry.get())
        Lk = float(self.Lk_entry.get())
        Ls = float(self.Ls_entry.get())
        a = float(self.a_entry.get())
        dok = float(self.dok_entry.get())
        włókno = str(self.włókno_entry.get())
        typ = str(self.typ_entry.get())
        dok_promienia = int(self.promien_dok_entry.get())
        rozklad(włókno,parm,Lp,Lk,Ls,a,dok,typ,dok_promienia)
        
        
    def wykres_dyspersja_but(self):
        parm = int(self.parm_entry.get())
        Lp = float(self.Lp_entry.get())
        Lk = float(self.Lk_entry.get())
        Ls = float(self.Ls_entry.get())
        a = float(self.a_entry.get())
        dok = float(self.dok_entry.get())
        włókno = str(self.włókno_entry.get())
        typ = str(self.typ_entry.get())
        dyspersja(włókno,parm,Lp,Lk,Ls,a,dok,typ)
        
        
    def wykres_pola_but(self):
        parm = int(self.parm_entry.get())
        Lp = float(self.Lp_entry.get())
        Lk = float(self.Lk_entry.get())
        Ls = float(self.Ls_entry.get())
        a = float(self.a_entry.get())
        dok = float(self.dok_entry.get())
        włókno = str(self.włókno_entry.get())
        typ = str(self.typ_entry.get())

        pola(włókno,parm,Lp,Lk,Ls,a,dok,typ)
      
    def wykres_stala_prop_but(self):
        parm = int(self.parm_entry.get())
        Lp = float(self.Lp_entry.get())
        Lk = float(self.Lk_entry.get())
        Ls = float(self.Ls_entry.get())
        a = float(self.a_entry.get())
        dok = float(self.dok_entry.get())
        włókno = str(self.włókno_entry.get())
        typ = str(self.typ_entry.get())
        stalaprop(włókno,parm,Lp,Lk,Ls,a,dok,typ)
        
    def wykresmodybut(self):
        parm = int(self.parm_entry.get())
        Lp = float(self.Lp_entry.get())
        Lk = float(self.Lk_entry.get())
        Ls = float(self.Ls_entry.get())
        a = float(self.a_entry.get())
        dok = float(self.dok_entry.get())
        włókno = str(self.włókno_entry.get())
        wykresymody(włókno,parm,Lp,Lk,Ls,a,dok)
             
    def wykresneffbut(self): 
        parm = int(self.parm_entry.get())
        Lp = float(self.Lp_entry.get())
        Lk = float(self.Lk_entry.get())
        Ls = float(self.Ls_entry.get())
        a = float(self.a_entry.get())
        dok = float(self.dok_entry.get())
        włókno = str(self.włókno_entry.get())
        typ = str(self.typ_entry.get())
        danymod(włókno,parm,Lp,Lk,Ls,a,dok,typ)
            
    def potw_mz(self):
        
        parm = int(self.parm_entry.get())
        a = float(self.a_entry.get())
        dok = float(self.dok_entry.get())
        Lp = float(self.Lp_entry.get())
        włókno = str(self.włókno_entry.get())
        Hondros4(włókno,parm,Lp,a,dok)

   
    def okno_wynik(self):
        parm = int(self.parm_entry.get())
        a = float(self.a_entry.get())
        dok = float(self.dok_entry.get())
        Lp = float(self.Lp_entry.get())
        włókno = str(self.włókno_entry.get())
        V = czestotliwosc(włókno,parm,Lp,a,dok)
        wynik = Znalezione(włókno,parm,Lp,a,dok)  
        self.otworz_okienko_z_wynikiem(wynik,V)
        

    def otworz_okienko_z_wynikiem(self,wynik,V):
        okno_wynik = tk.Toplevel(root)
        okno_wynik.title("Wynik obliczeń")
            
        for mod in wynik:
            info_label = tk.Label(okno_wynik, text=f"Znalezione mody:")
            info_label.grid(row=0, column=1, padx=5, pady=5) 
            
            wynik_label = tk.Label(okno_wynik, text=f"{mod}",wraplength=500)
            wynik_label.grid(row=wynik.index(mod)+1, column=1, padx=5, pady=5)    
        V_label = tk.Label(okno_wynik, text=f"Znormalizowana częstotliwość = {V}",wraplength=500)
        V_label.grid(row=len(wynik)+1, column=1, padx=5, pady=5)
            
        zamknij_okno_wynik = tk.Button(okno_wynik, text="Zamknij", command=okno_wynik.destroy)
        zamknij_okno_wynik.grid(row=1, column=2, padx=5, pady=5)
        
    def otworz_informacja_m(self):
        okno_info_m = tk.Toplevel(root)
        okno_info_m.title("Informacja o parametrze m ")
        okno_info_m.geometry("400x200")
        wynik_label = tk.Label(okno_info_m, text=f"Parametr m jest liczbą modową / rzędem modów dla których będą szukane mody.",wraplength=300, 
        justify="center", 
        font=("Arial", 12))

        wynik_label.grid(row=1, column=1, padx=5, pady=5)
            
        zamknij_okno_wynik = tk.Button(okno_info_m, text="Zamknij", command=okno_info_m.destroy)
        zamknij_okno_wynik.grid(row=1, column=2, padx=5, pady=5)    
   
    def otworz_informacja_lambda(self):
        okno_info_lambda = tk.Toplevel(root)
        okno_info_lambda.title("Informacja o parametrze długości fali ")
        okno_info_lambda.geometry("400x200")
        wynik_label = tk.Label(okno_info_lambda, text=f"Tu należy podać zakres długości fali, dla których będą znajdywane mody. Pierwsze pole oznacza początek zakresu, drugie krok, trzecie koniec zakresu. W przypadku wykresów wartości Hondrosa-Debye'a, oraz wykresów rozkładów pola, pod uwagę brana jest wartość początkowa zakresu",wraplength=300, 
        justify="center", 
        font=("Arial", 12))

        wynik_label.grid(row=1, column=1, padx=5, pady=5)
            
        zamknij_okno_wynik = tk.Button(okno_info_lambda, text="Zamknij", command=okno_info_lambda.destroy)
        zamknij_okno_wynik.grid(row=1, column=2, padx=5, pady=5)    
   
    def otworz_informacja_promien(self):
        okno_info_promien = tk.Toplevel(root)
        okno_info_promien.title("Informacja o parametrze promień ")
        okno_info_promien.geometry("400x200")
        wynik_label = tk.Label(okno_info_promien, text=f"Promień rdzenia podawany w mikrometrach.",wraplength=300, 
        justify="center", 
        font=("Arial", 12))

        wynik_label.grid(row=1, column=1, padx=5, pady=5)       
        zamknij_okno_wynik = tk.Button(okno_info_promien, text="Zamknij", command=okno_info_promien.destroy)
        zamknij_okno_wynik.grid(row=1, column=2, padx=5, pady=5)  
              
    def otworz_informacja_wlokno(self):
        okno_info_wlokno = tk.Toplevel(root)
        okno_info_wlokno.title("Informacja o parametrze włókno ")
        okno_info_wlokno.geometry("400x200")
        wynik_label = tk.Label(okno_info_wlokno, text=f"Wybierz włókno dla którego chcesz otrzymać wyniki. Można dodać własne włókno o zadanych parametrach w pliku fibers.py oraz funkcje_dysp.py do wykresów dyspersji.",wraplength=300, 
        justify="center", 
        font=("Arial", 12))

        wynik_label.grid(row=1, column=1, padx=5, pady=5)       
        zamknij_okno_wynik = tk.Button(okno_info_wlokno, text="Zamknij", command=okno_info_wlokno.destroy)
        zamknij_okno_wynik.grid(row=1, column=2, padx=5, pady=5)    
        
        
    def otworz_informacja_dok(self):
        okno_info_dok = tk.Toplevel(root)
        okno_info_dok.title("Informacja o parametrze krok ")
        okno_info_dok.geometry("400x200")
        wynik_label = tk.Label(okno_info_dok, text=f"Krok decyduje o tym z jaką dokładnością znajdywane będą miejsca, w których funckja Hondrosa-Debye'a zmienia znak, gdzie liczone będą miejsca zerowe, a co za tym idzie mody prowadzone w światłowodzie. Zalecane jest podać wartości niebędące dzielnikami potęg dziesiątki np. 0.0000011",wraplength=300, 
        justify="center", 
        font=("Arial", 12))

        wynik_label.grid(row=1, column=1, padx=5, pady=5)       
        zamknij_okno_wynik = tk.Button(okno_info_dok, text="Zamknij", command=okno_info_dok.destroy)
        zamknij_okno_wynik.grid(row=1, column=2, padx=5, pady=5) 
        
    def otworz_informacja_typ(self):
        okno_info_typ = tk.Toplevel(root)
        okno_info_typ.title("Typ")
        okno_info_typ.geometry("400x200")
        wynik_label = tk.Label(okno_info_typ, text=f"W tym polu podać można dla jakiego typu modów wyświetlone zostaną wykresy. Pole przyjmuje wartości: All - wyświetlenie wszystkich modów, TM, TE, EH i HE. Istnieje możliwość podania konkretnego modu przykładowo: EH3_1.",wraplength=300, 
        justify="center", 
        font=("Arial", 12))

        wynik_label.grid(row=1, column=1, padx=5, pady=5)       
        zamknij_okno_wynik = tk.Button(okno_info_typ, text="Zamknij", command=okno_info_typ.destroy)
        zamknij_okno_wynik.grid(row=1, column=2, padx=5, pady=5) 
   
   
    def otworz_informacja_wykreszera(self):
        okno_info_wykreszera = tk.Toplevel(root)
        okno_info_wykreszera.title("Informacja o wykresie wartości Hondrosa-Debye'a")
        okno_info_wykreszera.geometry("400x200")
        wynik_label = tk.Label(okno_info_wykreszera, text=f"Wykres wartości Hondrosa Debye'a dla zadanych parametrów ze znalezionymi miejscami zerowymi. Wykres przedstawia sposób w jaki znajdywane są efektywne współczynniki załamania poszczególnych modów, dla danej długości fali.",wraplength=300, 
        justify="center", 
        font=("Arial", 12))

        wynik_label.grid(row=1, column=1, padx=5, pady=5)       
        zamknij_okno_wynik = tk.Button(okno_info_wykreszera, text="Zamknij", command=okno_info_wykreszera.destroy)
        zamknij_okno_wynik.grid(row=1, column=2, padx=5, pady=5) 
   
    def otworz_informacja_wykresstala(self):
        okno_info_wykresstala = tk.Toplevel(root)
        okno_info_wykresstala.title("Informacja o wykresach stałej propagacji ")
        okno_info_wykresstala.geometry("400x200")
        wynik_label = tk.Label(okno_info_wykresstala, text=f"Wykresy przedstawiają zależność stałej propagacji danego modu od długości fali oraz od częstotliwości dali.",wraplength=300, 
        justify="center", 
        font=("Arial", 12))

        wynik_label.grid(row=1, column=1, padx=5, pady=5)       
        zamknij_okno_wynik = tk.Button(okno_info_wykresstala, text="Zamknij", command=okno_info_wykresstala.destroy)
        zamknij_okno_wynik.grid(row=1, column=2, padx=5, pady=5) 
        
    def otworz_informacja_wykresneff(self):
        okno_info_wykresneff = tk.Toplevel(root)
        okno_info_wykresneff.title("Informacja o wykresach efektywnych współczynników załamania")
        okno_info_wykresneff.geometry("400x200")
        wynik_label = tk.Label(okno_info_wykresneff, text=f"Wykresy przedstwiające efektywe współczynniki załamania posortowane w poszczególne mody, w zadanym zakresie długości fal.",wraplength=300, 
        justify="center", 
        font=("Arial", 12))

        wynik_label.grid(row=1, column=1, padx=5, pady=5)       
        zamknij_okno_wynik = tk.Button(okno_info_wykresneff, text="Zamknij", command=okno_info_wykresneff.destroy)
        zamknij_okno_wynik.grid(row=1, column=2, padx=5, pady=5) 
        
    def otworz_informacja_wykresamplitudy(self):
        okno_info_wykresamplitudy = tk.Toplevel(root)
        okno_info_wykresamplitudy.title("Informacja o wykresach składowych pola i rozkładów pola. ")
        okno_info_wykresamplitudy.geometry("400x200")
        wynik_label = tk.Label(okno_info_wykresamplitudy, text=f"Wykresy przedstawiają zależność poszczególnych składowych pola od promienia, oraz obrazy rozkładów natężeń poszczególnych składowych pól w zależności od kąta wokół osi i odległości od promienia.",wraplength=300, 
        justify="center", 
        font=("Arial", 12))

        wynik_label.grid(row=1, column=1, padx=5, pady=5)       
        zamknij_okno_wynik = tk.Button(okno_info_wykresamplitudy, text="Zamknij", command=okno_info_wykresamplitudy.destroy)
        zamknij_okno_wynik.grid(row=1, column=2, padx=5, pady=5)    
        
    def otworz_informacja_znalezione(self):
        okno_info_znalezione = tk.Toplevel(root)
        okno_info_znalezione.title("Informacja o znalezionych modach ")
        okno_info_znalezione.geometry("400x200")
        wynik_label = tk.Label(okno_info_znalezione, text=f"Po nacieśnięciu przycisku Pokaż Wyniki wyświetlone zostaną wszystkie znalezione mody dla długości fali zadanej poprzez początek zakresu.",wraplength=300, 
        justify="center", 
        font=("Arial", 12))

        wynik_label.grid(row=1, column=1, padx=5, pady=5)       
        zamknij_okno_wynik = tk.Button(okno_info_znalezione, text="Zamknij", command=okno_info_znalezione.destroy)
        zamknij_okno_wynik.grid(row=1, column=2, padx=5, pady=5)    
        
    def pobierz_wlokna(self, modul):
        wlokna = [name for name, obj in inspect.getmembers(modul, inspect.isclass)]
        return wlokna
   
    def otworz_informacja_dyspersja(self):
        okno_info_wykresamplitudy = tk.Toplevel(root)
        okno_info_wykresamplitudy.title("Informacja o włączeniu wykresów dyspersji. ")
        okno_info_wykresamplitudy.geometry("400x200")
        wynik_label = tk.Label(okno_info_wykresamplitudy, text=f"Wykresy dyspersji materiałowej oraz dyspersji modowej zadanego włókna dla poszczegónych modów, w zadanym zakresie długości fali.",wraplength=300, 
        justify="center", 
        font=("Arial", 12))

        wynik_label.grid(row=1, column=1, padx=5, pady=5)       
        zamknij_okno_wynik = tk.Button(okno_info_wykresamplitudy, text="Zamknij", command=okno_info_wykresamplitudy.destroy)
        zamknij_okno_wynik.grid(row=1, column=2, padx=5, pady=5)    
        


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
