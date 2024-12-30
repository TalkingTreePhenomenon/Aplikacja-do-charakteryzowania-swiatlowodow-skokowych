import numpy as np


class Włókno13_5Ge:
    def __init__(self, wavelength,a):
      
        self.wavelength = wavelength 
        self.a = a
        self.n_c = self.core_refractive_index(wavelength)  
        self.n_a = self.cladding_refractive_index(wavelength)
        self.info = f"Włókno $Si0_2$ z domieszką 13.5% $Ge0_2$ i promieniu rdzenia {a}$\mu$m"
       
    def core_refractive_index(self,wavelength):
        A1, A2, A3 = 0.711040, 0.451885, 0.704048
        B1, B2, B3 = 0.06427**2, 0.129408**2, 9.425478**2
        lambda_sq = wavelength ** 2
        n_c = 1 + (A1 * lambda_sq)/(lambda_sq - B1)+(A2*lambda_sq)/(lambda_sq - B2)+(A3 * lambda_sq)/(lambda_sq - B3)
        return np.sqrt(n_c)
    
        
    def cladding_refractive_index(self,wavelength):
      
        A1, A2, A3 = 0.6961663, 0.4079426, 0.8974994
        B1, B2, B3 = 0.0684043**2, 0.1162414**2, 9.896161**2
        lambda_sq = wavelength ** 2
        n_a = 1 + (A1 * lambda_sq)/(lambda_sq - B1)+(A2 * lambda_sq)/(lambda_sq - B2)+(A3 * lambda_sq)/(lambda_sq - B3)
        return np.sqrt(n_a)
    
    
class Włókno3_1Ge:
    def __init__(self, wavelength,a):
      
        self.wavelength = wavelength 
        self.a = a
        self.n_c = self.core_refractive_index(wavelength)  
        self.n_a = self.cladding_refractive_index(wavelength)
        self.info = f"Włókno $Si0_2$ z domieszką 3.1% $Ge0_2$ i promieniu rdzenia {a}$\mu$m" 
    def core_refractive_index(self,wavelength):
        A1, A2, A3 = 0.7028554, 0.4146307, 0.897454
        B1, B2, B3 = 0.0727723**2, 0.1143085**2, 9.896161**2
        lambda_sq = wavelength ** 2
        n_c = 1 + (A1 * lambda_sq) / (lambda_sq - B1) + (A2 * lambda_sq) / (lambda_sq - B2) + (A3 * lambda_sq) / (lambda_sq - B3)
        return np.sqrt(n_c)
        
    def cladding_refractive_index(self,wavelength):
      
        A1, A2, A3 = 0.6961663, 0.4079426, 0.8974994
        B1, B2, B3 = 0.0684043**2, 0.1162414**2, 9.896161**2
        lambda_sq = wavelength ** 2
        n_a = 1 + (A1 * lambda_sq) / (lambda_sq - B1) + (A2 * lambda_sq) / (lambda_sq - B2) + (A3 * lambda_sq) / (lambda_sq - B3)
        return np.sqrt(n_a)
    
    

class Włókno5_8Ge:
    def __init__(self, wavelength,a):
      
        self.wavelength = wavelength 
        self.a = a
        self.n_c = self.core_refractive_index(wavelength)  
        self.n_a = self.cladding_refractive_index(wavelength)
        self.info = f"Włókno $Si0_2$ z domieszką 5.8% $Ge0_2$ i promieniu  rdzenia {a}$\mu$m"
       
    def core_refractive_index(self,wavelength):
        A1, A2, A3 = 0.7088876, 0.4206803, 0.8956551
        B1, B2, B3 = 0.0609053**2, 0.1254514**2, 9.896162**2
        
        lambda_sq = wavelength ** 2
        n_c = 1 + (A1 * lambda_sq) / (lambda_sq - B1) + (A2 * lambda_sq) / (lambda_sq - B2) + (A3 * lambda_sq) / (lambda_sq - B3)
        
        return np.sqrt(n_c)
        
    def cladding_refractive_index(self,wavelength):
      
        A1, A2, A3 = 0.6961663, 0.4079426, 0.8974994
        B1, B2, B3 = 0.0684043**2, 0.1162414**2, 9.896161**2
        lambda_sq = wavelength ** 2
        n_a = 1 + (A1 * lambda_sq) / (lambda_sq - B1) + (A2 * lambda_sq) / (lambda_sq - B2) + (A3 * lambda_sq) / (lambda_sq - B3)
        return np.sqrt(n_a)
   
    
    
class Włókno7_9Ge:
    def __init__(self, wavelength,a):
      
        self.wavelength = wavelength 
        self.a = a
        self.n_c = self.core_refractive_index(wavelength)  
        self.n_a = self.cladding_refractive_index(wavelength)
        self.info = f"Włókno $Si0_2$ z domieszką 7.9% $Ge0_2$ i promieniu rdzenia {a}$\mu$m" 
       
    def core_refractive_index(self,wavelength):
        A1, A2, A3 = 0.7136824, 0.4254807, 0.8964226
        B1, B2, B3 = 0.0617167**2, 0.1270814**2, 9.896161**2
        lambda_sq = wavelength ** 2
        n_c = 1 + (A1 * lambda_sq) / (lambda_sq - B1) + (A2 * lambda_sq) / (lambda_sq - B2) + (A3 * lambda_sq) / (lambda_sq - B3)
        return np.sqrt(n_c)
        
    def cladding_refractive_index(self,wavelength):
        
        A1, A2, A3 = 0.6961663, 0.4079426, 0.8974994
        B1, B2, B3 = 0.0684043**2, 0.1162414**2, 9.896161**2
        lambda_sq = wavelength ** 2
        n_a = 1 + (A1 * lambda_sq) / (lambda_sq - B1) + (A2 * lambda_sq) / (lambda_sq - B2) + (A3 * lambda_sq) / (lambda_sq - B3)
        return np.sqrt(n_a)
    

class Włókno1F:
    def __init__(self, wavelength,a):
      
        self.wavelength = wavelength 
        self.a = a
        self.n_c = self.core_refractive_index(wavelength)  
        self.n_a = self.cladding_refractive_index(wavelength)
        self.info = f"Włókno $Si0_2$ z domieszką 7.9% $Ge0_2$ i promieniu rdzenia {a}$\mu$m" 
       
    def core_refractive_index(self,wavelength):
        A1, A2, A3 = 0.6961663, 0.4079426, 0.8974994
        B1, B2, B3 = 0.0684043**2, 0.1162414**2, 9.896161**2
        lambda_sq = wavelength ** 2
        n_c = 1 + (A1 * lambda_sq) / (lambda_sq - B1) + (A2 * lambda_sq) / (lambda_sq - B2) + (A3 * lambda_sq) / (lambda_sq - B3)
        return np.sqrt(n_c)
        
    def cladding_refractive_index(self,wavelength):
        
        A1, A2, A3 = 0.69325, 0.3972, 0.86008
        B1, B2, B3 = 0.06724**2, 0.11714**2, 9.7761**2
        lambda_sq = wavelength ** 2
        n_a = 1 + (A1 * lambda_sq) / (lambda_sq - B1) + (A2 * lambda_sq) / (lambda_sq - B2) + (A3 * lambda_sq) / (lambda_sq - B3)
        return np.sqrt(n_a)

class Włókno2F:
    def __init__(self, wavelength,a):
      
        self.wavelength = wavelength 
        self.a = a
        self.n_c = self.core_refractive_index(wavelength)  
        self.n_a = self.cladding_refractive_index(wavelength)
        self.info = f"Włókno $Si0_2$ z domieszką 7.9% $Ge0_2$ i promieniu rdzenia {a}$\mu$m" 
       
    def core_refractive_index(self,wavelength):
        A1, A2, A3 = 0.6961663, 0.4079426, 0.8974994
        B1, B2, B3 = 0.0684043**2, 0.1162414**2, 9.896161**2
        lambda_sq = wavelength ** 2
        n_c = 1 + (A1 * lambda_sq) / (lambda_sq - B1) + (A2 * lambda_sq) / (lambda_sq - B2) + (A3 * lambda_sq) / (lambda_sq - B3)
        return np.sqrt(n_c)
        
    def cladding_refractive_index(self,wavelength):
        
        A1, A2, A3 = 0.67744, 0.40101, 0.87193
        B1, B2, B3 = 0.06135**2, 0.1203**2, 9.8563**2
        lambda_sq = wavelength ** 2
        n_a = 1 + (A1 * lambda_sq) / (lambda_sq - B1) + (A2 * lambda_sq) / (lambda_sq - B2) + (A3 * lambda_sq) / (lambda_sq - B3)
        return np.sqrt(n_a)
    
    
class WłóknoUniwersalne:
    
    def __init__(self, wavelength,a):
      
        self.wavelength = wavelength 
        self.a = a
        self.n_c = self.core_refractive_index()  
        self.n_a = self.cladding_refractive_index()
        self.info = "Włókno o stałych współczynnikach załamania" 
    def core_refractive_index(self):
       
        
        
        n_c = 1.45
        return n_c

    def cladding_refractive_index(self):
      
       
        n_a = 1.44  
        return n_a
    
    