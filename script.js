function generarCodigo() {
    const seleccion = document.getElementById('seleccion').value;
    const cruce = document.getElementById('cruce').value;
    const mutacion = document.getElementById('mutacion').value;
    const reemplazo = document.getElementById('reemplazo').value;
    const poblacion = document.getElementById('poblacion').value;
    const generaciones = document.getElementById('generaciones').value;
    const p_cruce = document.getElementById('p_cruce').value;
    const p_mutacion = document.getElementById('p_mutacion').value;
    const aptitud = document.getElementById('aptitud').value;

    const codigo = `from algoritmos_geneticos_DG_PV.genetico import AlgoritmoGenetico\n\n` +
                   `aptitud = ${aptitud}\n\n` +
                   `algoritmo = AlgoritmoGenetico(\n` +
                   `    tamaño_poblacion=${poblacion},\n` +
                   `    num_generaciones=${generaciones},\n` +
                   `    funcion_fitness=aptitud,\n` +
                   `    metodo_seleccion='${seleccion}',\n` +
                   `    metodo_cruce='${cruce}',\n` +
                   `    metodo_mutacion='${mutacion}',\n` +
                   `    metodo_reemplazo='${reemplazo}',\n` +
                   `    probabilidad_cruce=${p_cruce},\n` +
                   `    probabilidad_mutacion=${p_mutacion}\n` +
                   `)\n\n` +
                   `algoritmo.inicializar_poblacion(tamaño_genoma=10)\n` +
                   `algoritmo.evolucionar()\n` +
                   `mejor, puntuacion = algoritmo.obtener_mejor_individuo()\n` +
                   `print(f"Mejor individuo: {mejor}, Aptitud: {puntuacion}")`;

    const codeElement = document.getElementById('codigo_generado');
    codeElement.textContent = codigo;
    hljs.highlightElement(codeElement);
}

function copiarCodigo() {
    const codigo = document.getElementById('codigo_generado').innerText;
    navigator.clipboard.writeText(codigo).then(() => {
        alert('Código copiado al portapapeles');
    }).catch(err => {
        console.error('Error al copiar el código: ', err);
    });
}

function copiarCodigoC(boton) {
    const code = boton.nextElementSibling.innerText;
    navigator.clipboard.writeText(code).then(() => {
      boton.innerText = "¡Copiado!";
      setTimeout(() => (boton.innerText = "Copiar"), 2000);
    });
  }
