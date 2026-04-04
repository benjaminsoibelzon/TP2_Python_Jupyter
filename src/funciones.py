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


def analizar_playlist(playlist: list):
    """
    Recibe una lista de canciones con duración 'm:ss' y devuelve:
    - total_minutos
    - total_segundos
    - canción más larga (dict)
    - canción más corta (dict)
    """

    total_segundos = 0

    # Convertir cada duración a segundos
    for song in playlist:
        minutos, segundos = map(int, song["duration"].split(":"))
        dur_total = minutos * 60 + segundos
        song["duration_seconds"] = dur_total
        total_segundos += dur_total

    # Calcular totales
    total_minutos = total_segundos // 60
    resto_segundos = total_segundos % 60

    # Encontrar max y min
    mas_larga = max(playlist, key=lambda x: x["duration_seconds"])
    mas_corta = min(playlist, key=lambda x: x["duration_seconds"])

    return total_minutos, resto_segundos, mas_larga, mas_corta

def filtrar_spoilers(texto, spoilers):
    resultado = texto
    for palabra in spoilers:
        palabra = palabra.strip()
        if palabra == "":
            continue
        reemplazo = "*" * len(palabra)
        resultado = resultado.replace(palabra, reemplazo)
        resultado = resultado.replace(palabra.lower(), reemplazo)
        resultado = resultado.replace(palabra.upper(), reemplazo)
        resultado = resultado.replace(palabra.capitalize(), reemplazo)
    return resultado