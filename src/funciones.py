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

def validar_email(email):
    # 1. Contiene exactamente un @
    if email.count("@") != 1:
        return False

    parte_izq, parte_der = email.split("@")

    # 2. Tiene al menos un carácter antes del @
    if len(parte_izq) == 0:
        return False

    # 3. No empieza ni termina con @ ni con .
    if email.startswith("@") or email.endswith("@") or email.startswith(".") or email.endswith("."):
        return False

    # 4. Tiene al menos un punto después del @
    if "." not in parte_der:
        return False

    # 5. La parte después del último punto tiene al menos 2 caracteres
    dominio = parte_der.split(".")[-1]
    if len(dominio) < 2:
        return False

    return True

def calcular_envio(peso, zona):
    zona = zona.lower()

    # Validar zona
    if zona not in ["local", "regional", "nacional"]:
        return None  # señal de zona inválida

    # Determinar costo según peso
    if peso <= 1:
        costos = {"local": 500, "regional": 1000, "nacional": 2000}
    elif peso <= 5:
        costos = {"local": 1000, "regional": 2500, "nacional": 4500}
    else:
        costos = {"local": 2000, "regional": 5000, "nacional": 8000}

    return costos[zona]