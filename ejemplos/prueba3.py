import random
import matplotlib.pyplot as plt
from algoritmos_geneticos_DG_PV.genetico import AlgoritmoGenetico

# 🔥 1. Datos del problema
pesos = [12, 7, 11, 8, 9, 6, 14, 7, 5, 3]
valores = [24, 13, 23, 15, 16, 10, 28, 14, 12, 6]
capacidad_mochila = 35

# 🔥 2. Función de aptitud
def funcion_fitness(individuo):
    peso_total = sum(p * g for p, g in zip(pesos, individuo))
    valor_total = sum(v * g for v, g in zip(valores, individuo))
    
    if peso_total > capacidad_mochila:
        return 0  # Penalización: si se pasa de peso, aptitud cero
    else:
        return valor_total

# 🔥 3. Configuración del Algoritmo Genético
algoritmo = AlgoritmoGenetico(
    tamaño_poblacion=50,
    num_generaciones=100,
    funcion_fitness=funcion_fitness,
    metodo_seleccion='torneo',
    metodo_cruce='un_punto',
    metodo_mutacion='basica',
    metodo_reemplazo='elitismo',
    probabilidad_cruce=0.8,
    probabilidad_mutacion=0.05
)

# 🔥 4. Inicializamos la población
# Cada individuo es un vector binario de 10 genes (1 = llevar objeto, 0 = no llevar)
algoritmo.inicializar_poblacion(tamaño_genoma=len(pesos))

# 🔥 5. Evolucionamos y guardamos la historia
mejores_valores = []

for gen in range(algoritmo.num_generaciones):
    algoritmo.evolucionar()
    mejor, valor = algoritmo.obtener_mejor_individuo()
    mejores_valores.append(valor)

# 🔥 6. Mostramos resultados finales
mejor, mejor_valor = algoritmo.obtener_mejor_individuo()
peso_final = sum(p * g for p, g in zip(pesos, mejor))

print("\n🎒 Mejor combinación encontrada:")
for idx, gen in enumerate(mejor):
    if gen == 1:
        print(f"Objeto {idx+1}: Peso={pesos[idx]}, Valor={valores[idx]}")

print(f"\nPeso total: {peso_final}")
print(f"Valor total: {mejor_valor}")

# 🔥 7. Visualizamos evolución
plt.plot(mejores_valores)
plt.title('Evolución del mejor valor obtenido')
plt.xlabel('Generaciones')
plt.ylabel('Mejor valor')
plt.grid(True)
plt.show()
