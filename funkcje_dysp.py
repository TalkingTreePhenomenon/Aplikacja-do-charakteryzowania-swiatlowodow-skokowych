import numpy as np
import matplotlib.pyplot as plt
import sympy as sp




class Włókno13_5Ge:
    def __init__(self):
      
        self.wavelength = sp.Symbol('wavelength')
    
    def core_refractive_index(self,wavelength):
   
        A1, A2, A3 = 0.711040, 0.451885, 0.704048
        B1, B2, B3 = 0.06427**2, 0.129408**2, 9.425478**2
        
 
        n_c = sp.sqrt(1 + (A1 *  wavelength ** 2) / ( wavelength ** 2 - B1) + (A2 *  wavelength ** 2) / ( wavelength ** 2 - B2) + (A3 *  wavelength ** 2) / ( wavelength ** 2 - B3))
       
        return  n_c
    
    def group_refractive_index_derivative(self):
        n_c = self.core_refractive_index(self.wavelength)
        n_group = n_c - sp.diff(n_c, self.wavelength)
        n_c_modederivative = sp.diff(n_group, self.wavelength)
        return n_c_modederivative
    
    def core_refractive_index_derivative(self):
        n_c = self.core_refractive_index(self.wavelength)
        n_c_derivative = sp.diff(n_c, self.wavelength)  # Pierwsza pochodna
        n_c_derivative2 = sp.diff(n_c_derivative, self.wavelength)  # Druga pochodna
        
        return n_c_derivative2 
    
    
class Włókno3_1Ge:
    def __init__(self):
      
        self.wavelength = sp.Symbol('wavelength')
    def core_refractive_index(self,wavelength):
        
        A1, A2, A3 = 0.7028554, 0.4146307, 0.897454
        B1, B2, B3 = 0.0727723**2, 0.1143085**2, 9.896161**2
        
        n_c = sp.sqrt(1 + (A1 *  wavelength ** 2) / ( wavelength ** 2 - B1) + (A2 *  wavelength ** 2) / ( wavelength ** 2 - B2) + (A3 *  wavelength ** 2) / ( wavelength ** 2 - B3))
       
        return  n_c
    
    def group_refractive_index_derivative(self):
        n_c = self.core_refractive_index(self.wavelength)
        n_group = n_c - sp.diff(n_c, self.wavelength)
        n_c_modederivative = sp.diff(n_group, self.wavelength)
        return n_c_modederivative
    
    def core_refractive_index_derivative(self):
        n_c = self.core_refractive_index(self.wavelength)
        n_c_derivative = sp.diff(n_c, self.wavelength)  
        n_c_derivative2 = sp.diff(n_c_derivative, self.wavelength) 
        
        return n_c_derivative2 
    

class Włókno5_8Ge:
    def __init__(self):
      
        self.wavelength = sp.Symbol('wavelength') 
        
    def core_refractive_index(self,wavelength):  
        
        A1, A2, A3 = 0.7088876, 0.4206803, 0.8956551
        B1, B2, B3 = 0.0609053**2, 0.1254514**2, 9.896162**2
        
        
        n_c = sp.sqrt(1 + (A1 *  wavelength ** 2) / ( wavelength ** 2 - B1) + (A2 *  wavelength ** 2) / ( wavelength ** 2 - B2) + (A3 *  wavelength ** 2) / ( wavelength ** 2 - B3))
        return  n_c
    
    def group_refractive_index_derivative(self):
        n_c = self.core_refractive_index(self.wavelength)
        n_group = n_c - sp.diff(n_c, self.wavelength)
        n_c_modederivative = sp.diff(n_group, self.wavelength)
        return n_c_modederivative
    
    def core_refractive_index_derivative(self):
        n_c = self.core_refractive_index(self.wavelength)
        n_c_derivative = sp.diff(n_c, self.wavelength)  
        n_c_derivative2 = sp.diff(n_c_derivative, self.wavelength) 
        
        return n_c_derivative2 
    
class Włókno7_9Ge:
    def __init__(self):
        self.wavelength = sp.Symbol('wavelength')
        

    def core_refractive_index(self,wavelength):
  
        A1, A2, A3 = 0.7136824, 0.4254807, 0.8964226
        B1, B2, B3 = 0.0617167**2, 0.1270814**2, 9.896161**2
        

        n_c = sp.sqrt(1 + (A1 *  wavelength ** 2) / ( wavelength ** 2 - B1) + (A2 *  wavelength ** 2) / ( wavelength ** 2 - B2) + (A3 *  wavelength ** 2) / ( wavelength ** 2 - B3))
        return  n_c
    
    def group_refractive_index_derivative(self):
        n_c = self.core_refractive_index(self.wavelength)
        n_group = n_c - sp.diff(n_c, self.wavelength)
        n_c_modederivative = sp.diff(n_group, self.wavelength)
        return n_c_modederivative
    
    def core_refractive_index_derivative(self):
        n_c = self.core_refractive_index(self.wavelength)
        n_c_derivative = sp.diff(n_c, self.wavelength) 
        n_c_derivative2 = sp.diff(n_c_derivative, self.wavelength)  
        
        return n_c_derivative2 
class Włókno1F:
    def __init__(self):
        self.wavelength = sp.Symbol('wavelength')
        

    def core_refractive_index(self,wavelength):
  
        A1, A2, A3 = 0.6961663, 0.4079426, 0.8974994
        B1, B2, B3 = 0.0684043**2, 0.1162414**2, 9.896161**2
        

        n_c = sp.sqrt(1 + (A1 *  wavelength ** 2) / ( wavelength ** 2 - B1) + (A2 *  wavelength ** 2) / ( wavelength ** 2 - B2) + (A3 *  wavelength ** 2) / ( wavelength ** 2 - B3))
        return  n_c
    
    def group_refractive_index_derivative(self):
        n_c = self.core_refractive_index(self.wavelength)
        n_group = n_c - sp.diff(n_c, self.wavelength)
        n_c_modederivative = sp.diff(n_group, self.wavelength)
        return n_c_modederivative
    
    def core_refractive_index_derivative(self):
        n_c = self.core_refractive_index(self.wavelength)
        n_c_derivative = sp.diff(n_c, self.wavelength)  
        n_c_derivative2 = sp.diff(n_c_derivative, self.wavelength)  
        
        return n_c_derivative2 
class Włókno2F:
    def __init__(self):
        self.wavelength = sp.Symbol('wavelength')
        

    def core_refractive_index(self,wavelength):
  
        A1, A2, A3 = 0.6961663, 0.4079426, 0.8974994
        B1, B2, B3 = 0.0684043**2, 0.1162414**2, 9.896161**2
        

        n_c = sp.sqrt(1 + (A1 *  wavelength ** 2) / ( wavelength ** 2 - B1) + (A2 *  wavelength ** 2) / ( wavelength ** 2 - B2) + (A3 *  wavelength ** 2) / ( wavelength ** 2 - B3))
        return  n_c
    
    def group_refractive_index_derivative(self):
        n_c = self.core_refractive_index(self.wavelength)
        n_group = n_c - sp.diff(n_c, self.wavelength)
        n_c_modederivative = sp.diff(n_group, self.wavelength)
        return n_c_modederivative
    
    def core_refractive_index_derivative(self):
        n_c = self.core_refractive_index(self.wavelength)
        n_c_derivative = sp.diff(n_c, self.wavelength) 
        n_c_derivative2 = sp.diff(n_c_derivative, self.wavelength)  
        
        return n_c_derivative2 
  
    
    
    
class WłóknoUniwersalne:
    def __init__(self):

        self.n_c = self.core_refractive_index()  
        self.n_a = self.cladding_refractive_index()
    def core_refractive_index(self):
        
        n_c = 1.45
        return n_c

    def cladding_refractive_index(self):

        n_a = 1.44  
        return n_a