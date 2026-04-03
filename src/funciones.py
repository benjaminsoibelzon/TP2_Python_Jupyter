def analizar_texto(texto: str):
    """
    Recibe un string multilínea y devuelve:
    - total_lineas
    - total_palabras
    - promedio
    - lista de tuplas (linea, cantidad_palabras) por encima del promedio
    """
    lineas = texto.split('\n')
    total_lineas = len(lineas)

    palabras_en_cada_linea = [linea.split() for linea in lineas]
    total_palabras = sum(len(p) for p in palabras_en_cada_linea)

    promedio = total_palabras / total_lineas if total_lineas > 0 else 0

    lineas_sobre_promedio = []
    for linea in lineas:
        cant = len(linea.split())
        if cant > promedio:
            lineas_sobre_promedio.append((linea, cant))

    return total_lineas, total_palabras, promedio, lineas_sobre_promedio