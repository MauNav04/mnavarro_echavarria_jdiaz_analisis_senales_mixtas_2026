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
    lista_datos = []

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

    lista_datos.append(v_s)
    lista_datos.append(v_r)
    lista_datos.append(v_z_load)
    lista_datos.append(r)

    return lista_datos

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Función para dibujar circulo
# x = x_centro + rcos(theta)
# y = y_centro + rsen(theta)
# con theta de 0 a 2*pi
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def dibujar_circulo(x_centro, y_centro, r):

    # dibujar centro
    plt.scatter(x_centro, y_centro)

    theta = np.linspace(0, 2*np.pi, 1000) # arreglo de angulos de 0 a 2*pi

    circulo_x = x_centro + r*np.cos(theta)
    circulo_y = y_centro + r*np.sin(theta)

    lista_circulo = []
    
    lista_circulo.append(circulo_x)
    lista_circulo.append(circulo_y)

    plt.plot(circulo_x, circulo_y)
    plt.axis('equal') # mantener eje iguales

    return lista_circulo

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Función para encontrar el punto intermedio entre 2 circulos
# Fórmula: x_intermedio = x1 + a*(x2-x1)/d , y_intermedio = y1 + a*(y2-y1)/d
# con: d = sqrt((x2-x1)^2 + (y2-y1)^2) (magnitud)
# y con: a = ( r_1^2 - r_2^2 + d^2 ) / (2d)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def punto_intermedio(r1, r2, x1, x2, y1, y2):

    d = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    a = ( r1**2 - r2**2 + d**2 ) / (2*d)

    x_intermedio = x1 + a*(x2-x1)/d 
    y_intermedio = y1 + a*(y2-y1)/d

    plt.scatter(x_intermedio, y_intermedio) # dibujar el punto

    return a, x_intermedio, y_intermedio, d

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Función para encontrar intersecciones
# Fórmula: xi = x_intermedio +/- h*(y2-y1)/d, yi = y_intermedio -/+ h*(x2-x1)/d
# con: h = sqrt(r_1^2 - a^2)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def encontrar_intersecciones(r1, a, x_intermedio, y_intermedio, x1, x2, y2, y1, d):

    h = np.sqrt(r1**2 - a**2)

    xi1 = x_intermedio + h*(y2-y1)/d
    yi1 = y_intermedio - h*(x2-x1)/d

    xi2 = x_intermedio - h*(y2-y1)/d
    yi2 = y_intermedio + h*(x2-x1)/d

    # dibujar intersecciones
    plt.scatter(xi1, yi1) 
    plt.scatter(xi2, yi2)

    # dibujar linea hacia esas intersecciones
    plt.plot([x1, xi1], [y1, yi1])
    plt.plot([x1, xi2], [y1, yi2])
    plt.plot([x2, xi1], [y2, yi1])
    plt.plot([x2, xi2], [y2, yi2])

    return xi1, yi1, xi2, yi2

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Función para calcular impedancia
# Aun pendiente de desarrollar
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Programa Principal
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    lista_datos = pedir_datos() # 0 VS, 1 VR, 2 VZload, 3 R

    a, x_intermedio, y_intermedio, d = punto_intermedio(lista_datos[2], lista_datos[1], 
                                       lista_datos[0], 0, 0, 0) # r1, r2, x1 = 2, resto 0
    
    xi1, yi1, xi2, yi2 = encontrar_intersecciones(lista_datos[2], a, x_intermedio, y_intermedio, lista_datos[0], 0, 0, 0, d) # r1, ... , centro1, centro2, d

    dibujar_circulo(lista_datos[0], 0, lista_datos[2]) # circulo 1 -> VZload, centro 2,0 
    dibujar_circulo(0, 0, lista_datos[1]) # circulo 2 -> VR, centro 0,0

    plt.title("Gráfico: Circuito RL serie en CA") # titulo global
    plt.xlabel("Eje Real (Re)") # titulo de eje
    plt.ylabel("Eje Imaginario (Im)") # titulo de eje

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    #plt.legend()
    plt.grid()

    plt.show() # mostrar 