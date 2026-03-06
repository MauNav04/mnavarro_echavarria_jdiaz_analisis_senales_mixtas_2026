# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Imports
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import numpy as np
import matplotlib.pyplot as plt

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Sesión asincrónica - Semana 2
# CE-1110 Análisis de Señales Mixtas
# Jafet - Emanuel - Mauro
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Función para solicitar datos: VS, VR, VZload, R 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def pedir_datos():

    n = 0

    while n == 0:
        v_s = float(input("Ingresa el voltaje de la fuente VS: "))
        v_r = float(input("Ingresa el voltaje de la resistencia VR: "))
        v_z_load = float(input("Ingresa el voltaje de la carga inductiva VZLoad: "))
        r = float(input("Ingresa el valor de la resistencia R: "))

        # Validar que NO OCURRA VS > VR + VZLoad 

        aux = v_r + v_z_load

        if v_s > aux:
            print("\nPor favor ingrese datos que NO SEAN VS > VR + VZLoad \n")
            n = 0
        
        else:
            print("\nDatos aceptados \n")
            n = 1

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Función para calcular impedancia
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Programa Principal
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    pedir_datos()