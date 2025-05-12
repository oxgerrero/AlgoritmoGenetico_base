from algoritmos_geneticos_DG_PV.genetico import AlgoritmoGenetico

# Definir función de aptitud (fitness)
def aptitud(individuo):
    return sum(individuo)  # Ejemplo simple: maximizar número de 1s

# Inicializar el algoritmo
algoritmo = AlgoritmoGenetico(
    tamaño_poblacion=20,
    num_generaciones=50,
    funcion_fitness=aptitud,
    metodo_seleccion='torneo',
    metodo_cruce='un_punto',
    metodo_mutacion='basica',
    metodo_reemplazo='elitismo',
    probabilidad_cruce=0.8,
    probabilidad_mutacion=0.05
)

# Inicializar población (genomas de 10 genes)
algoritmo.inicializar_poblacion(tamaño_genoma=10)

# Evolucionar
algoritmo.evolucionar()

# Mostrar mejor individuo
mejor, puntuacion = algoritmo.obtener_mejor_individuo()
print(f"Mejor individuo: {mejor}, Aptitud: {puntuacion}")