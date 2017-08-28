
# Árbol fractal
# Por, Luis Gerardo Canales Ocampo.
# + Códigos, e info. en https://github.com/LuisCanalesPy/Python-Ciencia-Arte/
# Contacto: lgco@comunidad.unam.mx


# Se importan las paqueterías que se van a utilizar.


import numpy as np      # Paquetería con herramientas para hacer operaciones matemáticas.
from matplotlib import pyplot as plt # Módulo para representación gráfica de datos.
from matplotlib.path import Path     # Herramienta para dibujar segmentos de rectas, dados un conjunto de puntos.
import matplotlib.patches as patches # Herramienta necesaria para poder dibujar los segmentos de rectas sobre una imagen.




"""
linea_path(A,B,n)...Dibuja una línea entre los puntos A y B, 
modificando el grosor y colores dependiendo el nivel de recursión "n".
"""
def linea_path(A, B, n):

    # Se le indica a Python que las variables g_min, g_max y n_max serán definidas afuera de la función.
    global g_min, g_max, n_max
    
    # Primero se posiciona el pincel en el punto A, posteriormente se dibuja un segmento de recta hacia el punto B.
    vertices = [A, B]
    instrucciones = [1, 2]                
    
    # Se crea un objeto "Path" con los puntos e instrucciones para dibujar el  segmento de recta.
    segmento_instrucciones = Path(vertices, instrucciones) 

    # Elección del color dependiendo el nivel de recursión actual.
    if 4 > n: 
        colores = np.random.rand(3,1)     # Los últimos 3 niveles serán de colores aleatorios, codificados en RGB.
    else:
        colores = "#c0c0c0"               # El resto de niveles será "plateado", codificado en sistema HEX.

    
    # Cálculo del grosor
    grosor = g_min + (g_max - g_min)*(n/n_max)**2    

    # Se crea un objeto "PathPatch" utilizando el objeto "Path" creado en la línea 15...
    # ... el cual contiene la información necesaria para crear los segmentos.
    #  También se configuran los parámetros de color y grosor con los calculados previamente.
    recta = patches.PathPatch(segmento_instrucciones, edgecolor=colores, facecolor="none", lw=grosor)
    
    ax.add_patch(recta)          # Se agrega el segmento creado al lienzo llamado "ax".




"""
arbol_path(A, B, a, b, l, n) ... Algoritmo recursivo que construirá el árbol implementando la función "línea_path".

Condición inicial: Segmento de recta AB.
A = Primer punto que define al segmento de recta que será condición inicial.
B = Segundo punto que define al segmento de recta que será condición inicial.
a = Ángulo de rotación del segmento BC a dibujar, respecto al segmento AB.
b = Ángulo de rotación del segmento BD a dibujar, respecto al segmento AB.
l = Proporción de tamaño de los segmentos a dibujar, respecto al segmento que se usa como condición inicial.
n = Nivel de recursión.
"""

def arbol_path(A, B, a, b, l, n):
    
    # Se transforman los puntos "A" y "B" a Numpy Arrays, para realizar operaciones entre vectores.
    A = np.array(A)     
    B = np.array(B)
    
    # Se dibuja el segmento de recta entre los puntos A y B utilizando la función que se creo anteriormente.
    linea_path(A, B, n)      
    
    # Si  el nivel de recursión "n" es mayor a cero se calcula la posición de los puntos C y D...
    # ...para crear los segmentos del siguiente nivel de recursión.
    if n > 0:         
        
        C = B + l*np.dot( [[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]] , B - A )
        D = B + l*np.dot( [[np.cos(b), np.sin(b)], [-np.sin(b), np.cos(b)]] , B - A )
        
        # Se aplica el algoritmo recursivamente. Esta vez la condición inicial estará dada por los...
        # ...nuevos puntos calculados (C y D)  y el punto B.
        arbol_path(B, C, a, b, l, n-1)    
        arbol_path(B, D, a, b, l, n-1)    
        # Debe notarse que al aplicarse el algoritmo a los nuevos puntos...
        # ... se hace con un nivel de recursión menor. es decir "n-1".





# Se define un figura nueva, con fondo negro, y tamaño 10x10 pulgadas.
fig = plt.figure(figsize=(10,10), facecolor="black")

# Lienzo dentro de la figura, donde se dibujará directamente el árbol.
ax = fig.add_subplot(111)                                  

# Definición de parámetros
A = (0, 0)
B = (0, 1)
a = np.pi/8
b = np.pi/6
l = 0.8
n = 9

#Se le asignan valores a los parámetros para el control del grosor:
g_min = 1.5 ; g_max = 20 ; n_max = 10

# Se corre el algoritmo recursivo.
arbol_path(A, B, a, b, l, n)


ax.axis("square")                                  # Configura la misma escala en dirección horizontal y vertical.
ax.axis("off")                                     # Desactiva los ejes coordenados.
fig.tight_layout()                                 # Ajusta el tamaño del dibujo a la imagen.
plt.show()                                         # Muestra la imagen final




fig.savefig("arbol_fractal_tunneado.png", facecolor=fig.get_facecolor())   # Guarda el resultado en un archivo ".png"


