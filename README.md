# 🧬 algoritmos_geneticos_col

**Una librería de algoritmos genéticos modular y parametrizable, diseñada en español latino colombiano.**  
Ideal para optimización, inteligencia artificial evolutiva, proyectos de investigación y educación.

---

## 🚀 Características principales

- 📚 Métodos de selección: **Ruleta**, **Torneo**, **Aleatorio**.
- 🔀 Métodos de cruce: **Un punto**, **Dos puntos**, **Uniforme**.
- 🧬 Métodos de mutación: **Básica** y **Aleatoria**.
- 🔄 Métodos de reemplazo: **Generacional** y **Elitismo**.
- 🎯 Totalmente **parametrizable** (tamaño de población, tasa de cruce, tasa de mutación, generaciones, etc.).
- 🛠️ Código limpio, documentado y en **español latino**.

---

## 📦 Instalación

Una vez esté publicada en PyPI:

```bash
pip install algoritmos_geneticos_DG_PV
```

Por ahora, si deseas instalar localmente:

```bash
pip install .
```
Desde la raíz del proyecto donde está el `setup.py`.

---

## 🛠️ Ejemplo de uso básico

```python
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
```

---

## 📋 Documentación

- 📋 [Documentación completa](https://oxgerrero.github.io/AlgoritmoGenetico_base/) (en construcción).
- Código comentado directamente en cada módulo.
- Compatible con generación de documentación automática (`Sphinx`, `MkDocs`).

---

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**.  
Libre para uso, modificación y distribución con atribución.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!  
Puedes proponer mejoras, corregir errores o sugerir nuevos métodos evolutivos.

1. Haz un **fork** del proyecto.
2. Crea una **rama** (`git checkout -b mejora-nueva`).
3. Haz **commit** a tus cambios (`git commit -am 'nueva mejora'`).
4. Haz **push** (`git push origin mejora-nueva`).
5. Abre un **pull request**.

---

## 👨‍💻 Autor

- **David Gomez** - [GitHub](https://github.com/oxgerrero/)
- **Paula Vera** - [GitHub](https://github.com/paulav14/)
 
