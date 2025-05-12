import numpy as np
import matplotlib.pyplot as plt
from algoritmos_geneticos_DG_PV.genetico import AlgoritmoGenetico

# 🔥 1. Definimos cómo decodificar un individuo (binario) a números reales
def decodificar_individuo(individuo, rango=(-5, 5)):
    mitad = len(individuo) // 2
    x_bits = individuo[:mitad]
    y_bits = individuo[mitad:]
    
    x_decimal = int(''.join(str(bit) for bit in x_bits), 2)
    y_decimal = int(''.join(str(bit) for bit in y_bits), 2)
    
    max_decimal = (2 ** mitad) - 1
    
    x = rango[0] + (rango[1] - rango[0]) * (x_decimal / max_decimal)
    y = rango[0] + (rango[1] - rango[0]) * (y_decimal / max_decimal)
    
    return x, y

# 🔥 2. Definimos la función de aptitud
def funcion_fitness(individuo):
    x, y = decodificar_individuo(individuo)
    return np.sin(x) * np.cos(y) + x**2 - y**2

# 🔥 3. Configuramos el Algoritmo Genético
algoritmo = AlgoritmoGenetico(
    tamaño_poblacion=50,
    num_generaciones=100,
    funcion_fitness=funcion_fitness,
    metodo_seleccion='torneo',
    metodo_cruce='dos_puntos',
    metodo_mutacion='basica',
    metodo_reemplazo='elitismo',
    probabilidad_cruce=0.8,
    probabilidad_mutacion=0.02
)

# 🔥 4. Inicializamos la población
# Usamos 16 bits para representar x + 16 bits para y = 32 bits en total
algoritmo.inicializar_poblacion(tamaño_genoma=32)

# 🔥 5. Evolucionamos y guardamos la historia
mejores_aptitudes = []

for gen in range(algoritmo.num_generaciones):
    algoritmo.evolucionar()
    mejor, aptitud = algoritmo.obtener_mejor_individuo()
    mejores_aptitudes.append(aptitud)

# 🔥 6. Mostramos resultados finales
mejor, mejor_aptitud = algoritmo.obtener_mejor_individuo()
x, y = decodificar_individuo(mejor)

print("\n📈 Mejor solución encontrada:")
print(f"x = {x:.5f}, y = {y:.5f}")
print(f"f(x, y) = {mejor_aptitud:.5f}")

# 🔥 7. Visualizamos la evolución
plt.plot(mejores_aptitudes)
plt.title('Evolución de la mejor aptitud')
plt.xlabel('Generaciones')
plt.ylabel('Mejor aptitud')
plt.grid(True)
plt.show()
