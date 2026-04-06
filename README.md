# Trabajo Práctico – Python

Este proyecto contiene la resolución de 10 ejercicios utilizando modularización.  
Las funciones están en `src/funciones.py` y el notebook principal es `Notebooks/prueba.ipynb`.

## Requisitos

- Python 3.10 o superior
- Jupyter Notebook

Instalación de Jupyter:

pip install notebook

## Estructura del proyecto

TP2_PYTHON_JUPYTER/
│
├── Notebooks/
│   └── prueba.ipynb
│
├── src/
│   ├── funciones.py
│   ├── funciones_old.py
│   ├── __init__.py
│   └── __pycache__/
│
└── README.md

## Cómo ejecutar

1. Abrir la carpeta del proyecto.
2. Ejecutar en la terminal:

   jupyter notebook

3. Abrir el archivo Notebooks/prueba.ipynb.
4. Ejecutar la celda que agrega la ruta del módulo:

   import sys  
   sys.path.append("..\\src")

5. Ejecutar la celda de imports:

   from funciones import *

6. Ejecutar las celdas de cada ejercicio (1 al 10).

## Funciones incluidas

- Filtrado de spoilers  
- Validación de email  
- Cálculo de costo de envío  
- Análisis de hashtags  
- Sorteo de amigo invisible  
- Cifrado César  
- Normalización de registros de alumnos  
- Simulación de competencia de cocina (puntajes, rondas ganadas, ranking final)

## Datos
- Benjamin Soibelzon
- soibelzonben@gmail.com
- 018832/5

## Link Video Resolucion
- https://drive.google.com/file/d/1LVCxc-eOtw-ynbjlKzEQADxtaHK4f_gm/view?usp=sharing