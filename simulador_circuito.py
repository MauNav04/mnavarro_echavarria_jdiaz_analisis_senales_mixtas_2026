# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Imports
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

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
        print(' = '*50)
        v_s = float(input(" Ingresa el voltaje de la fuente VS: "))
        v_r = float(input(" Ingresa el voltaje de la resistencia VR: "))
        v_z_load = float(input(" Ingresa el voltaje de la carga inductiva VZLoad: "))
        r = float(input(" Ingresa el valor de la resistencia R: "))
        print(' = '*50)

        # Validar que NO OCURRA VS > VR + VZLoad 

        aux = v_r + v_z_load

        if v_s > aux:
            print("\n Por favor ingrese datos que NO SEAN VS > VR + VZLoad \n")
            n = 0
        
        else:
            print("\n Datos aceptados \n")
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

def dibujar_circulo(x_centro, y_centro, r, color):

    # dibujar centro
    plt.scatter(x_centro, y_centro, color=color)

    theta = np.linspace(0, 2*np.pi, 1000) # arreglo de angulos de 0 a 2*pi

    circulo_x = x_centro + r*np.cos(theta)
    circulo_y = y_centro + r*np.sin(theta)

    lista_circulo = []
    
    lista_circulo.append(circulo_x)
    lista_circulo.append(circulo_y)

    plt.plot(circulo_x, circulo_y, color=color, linestyle="--")
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

#    plt.scatter(x_intermedio, y_intermedio) # dibujar el punto

    return a, x_intermedio, y_intermedio, d

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Función para encontrar intersecciones
# Fórmula: xi = x_intermedio +/- h*(y2-y1)/d, yi = y_intermedio -/+ h*(x2-x1)/d
# con: h = sqrt(r_1^2 - a^2)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def encontrar_intersecciones(r1, r2, a, x_intermedio, y_intermedio, x1, x2, y2, y1, d):

    h = np.sqrt(r1**2 - a**2)

    xi1 = x_intermedio + h*(y2-y1)/d
    yi1 = y_intermedio - h*(x2-x1)/d

    xi2 = x_intermedio - h*(y2-y1)/d
    yi2 = y_intermedio + h*(x2-x1)/d

    # dibujar intersecciones
    plt.scatter(xi1, yi1) 
    plt.scatter(xi2, yi2)

    # puntos medios
    xm11 = ( x1 + xi1 ) / 2
    xm12 = ( x1 + xi2 ) / 2
    xm21 = ( x2 + xi1 ) / 2
    xm22 = ( x2 + xi2 ) / 2

    ym11 = ( y1 + yi1 ) / 2
    ym12 = ( y1 + yi2 ) / 2
    ym21 = ( y2 + yi1 ) / 2
    ym22 = ( y2 + yi2 ) / 2

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Angulos requeridos (usando arctan(y/x))
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    #x_vector11 = ( xi1 - x1 ) 
    #x_vector21 = ( xi1 - x2 ) 
    x_vector12 = ( x1 - xi2 ) 
    x_vector22 = ( xi2 - x2 ) 

    #y_vector11 = ( yi1 - y1 ) 
    #y_vector21 = ( y2 - yi1 ) 
    y_vector12 = ( yi2 - y1 ) 
    y_vector22 = ( yi2 - y2 )

    #theta11 = np.atan2(y_vector11, x_vector11)
    #theta21 = np.atan2(y_vector21, x_vector21)
    theta12 = np.atan2(y_vector12, x_vector12)
    theta22 = np.atan2(y_vector22, x_vector22)

    anguloVz = 0 - np.degrees(theta12) # -0 porque el vector va en la dirección contraria
    anguloVr = np.degrees(theta22)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Dibujar linea hacia esas intersecciones
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Circulo en 2,0
    plt.plot([x1, xi1], [y1, yi1], linestyle="--", color='gray') # VECTOR CAPACITIVO Vz
    plt.text(xm11+0.5, ym11, 'Vz en caso capacitivo', ha='center', va='center')

    plt.plot([xi2, x1], [yi2, y1], color='purple') # VECTOR INDUCTIVO Vz
    plt.text(xm12+0.5, ym12, f'VZload = {r1}, ángulo: {anguloVz:.2f}', ha='center', va='center', color='purple')

    # LINEA RECTA A PASAR POR VZ
    # Crear la ecuacion
    m = ( yi2 - y1 ) / (xi2 - x1)
    b = y1 - m*x1
    
    x = sp.Symbol('x')
    y = x*m + b
    f = sp.lambdify(x, y, 'numpy') # recta vz extendida

    y_perp = -x/m # recta perpendicular (por eso es -1/m) y que pasa por 0,0 (b = 0)
    f2 = sp.lambdify(x,y_perp, 'numpy')

    #Calcular interseccion del punto de las dos rectas
    x_inter_rect = (0 - b)/(m + 1/m)
    y_inter_rect = m*x_inter_rect + b
    plt.scatter(x_inter_rect, y_inter_rect, color='green')

    x_space2= np.linspace(0,x_inter_rect,1000)
    x_space = np.linspace(x_inter_rect, xi2,1000)

    plt.plot(x_space, f(x_space), linestyle="--", color='purple') # VECTOR CONTINUADO DE VZ (Resistencia parásita)
    plt.plot(x_space2, f2(x_space2), linestyle="--", color='pink') # VECTOR QUE SALE DEL ORIGEN (VL ideal)

    # Circulo en 0,0
    plt.plot([x2, xi1], [y2, yi1], linestyle="--", color='gray') # VECTOR CAPACITIVO Vr
    plt.text(xm21-0.5, ym21, 'Vr en caso capcitivo', ha='center', va='center')

    plt.plot([x2, xi2], [y2, yi2], color = 'orange') # VECTOR INDUCTIVO Vr
    plt.text(xm22-0.5, ym22, f'VR = {r2}, ángulo: {anguloVr:.2f}', ha='center', va='center', color='orange')

    return xi1, yi1, xi2, yi2, anguloVz, anguloVr

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Función para calcular impedancia
# Aun pendiente de desarrollar
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def impedancia(mag_v, mag_i, anguloV, anguloI):
    # Corriente V/R --> Impedancia: V/I
    # Como R = 1, V = I

    VR_rad = np.radians(anguloI)
    VZ_rad = np.radians(anguloV)

    # V = magnitud * (cos(theta) + j*sin(theta))

    Vz_complejo = mag_v * (np.cos(VZ_rad) + 1j*np.sin(VZ_rad))
    Ir_complejo = mag_i * (np.cos(VR_rad) + 1j*np.sin(VR_rad))

    Z_complejo = Vz_complejo/Ir_complejo

    print(' = '*50)
    print(' Por ley de Ohm, la corriente y el voltaje \n en la resistencia son las mismas (R=1) \n Así, se tiene que:')
    print(f' I = Vr/R \n I = {Ir_complejo:.2f} / 1 ohm \n I = {Ir_complejo:.2f}')
    print(' = '*50)
    print(' Por Ley de Ohm en la impedancia, \n dado que la corriente es la misma (circuito serie). ')
    print(f' Con VL = {Vz_complejo:.2f} \n y I = {Ir_complejo:.2f}, \n se tiene que:')
    print(' ZL = VL/I')
    print(f' ZL = {Z_complejo:.2f}')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Programa Principal
# Comando run: python3 simulador_circuito.py
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    lista_datos = pedir_datos() # [0] VS, [1] VR, [2] VZload, [3] R

    plt.plot([0, lista_datos[0]], [0,0], color='red')
    plt.text(0.8, -0.1, 'Vs = 2V', ha='center', va='center', color='red')

    dibujar_circulo(lista_datos[0], 0, lista_datos[2], "blue") # circulo 1 -> VZload, centro 2,0 
    dibujar_circulo(0, 0, lista_datos[1], "green") # circulo 2 -> VR, centro 0,0

    # Punto intermedio
    a, x_intermedio, y_intermedio, d = punto_intermedio(lista_datos[2], lista_datos[1], 
                                       lista_datos[0], 0, 0, 0) # r1, r2, x1 = 2, resto 0
    
    # Lineas hacia interseccion
    xi1, yi1, xi2, yi2, anguloVz, anguloVr = encontrar_intersecciones(lista_datos[2], lista_datos[1], a, x_intermedio, y_intermedio, 
                                                  lista_datos[0], 0, 0, 0, d) # r1, r2, ... , centro1, centro2, d
    
    impedancia(lista_datos[2], lista_datos[1], anguloVz, anguloVr) # por V/R = I, se tiene que la corriente serie es igual al voltaje en la resistencia

    plt.title("Gráfico: Circuito RL serie en CA") # titulo global
    plt.xlabel("Eje Real (Re)") # titulo de eje
    plt.ylabel("Eje Imaginario (Im)") # titulo de eje

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    #plt.legend()
    plt.grid()

    plt.show() # mostrar 