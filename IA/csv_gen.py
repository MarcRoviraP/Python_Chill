import pandas as pd
import numpy as np

# Columnas que quieres
variables = ["frecuencia", "tiempo_promedio_sesion", "acciones_totales", "recencia", "variabilidad"]

# Número de filas que quieres generar
num_filas = 1000  # puedes aumentar o disminuir según necesites

# Generar datos aleatorios realistas para cada columna
np.random.seed(42)  # para reproducibilidad
data_simulada = {
    "frecuencia": np.random.randint(1, 50, size=num_filas),  # veces que el usuario usa algo
    "tiempo_promedio_sesion": np.random.uniform(1, 60, size=num_filas),  # minutos
    "acciones_totales": np.random.randint(5, 500, size=num_filas),
    "recencia": np.random.randint(1, 365, size=num_filas),  # días desde última interacción
    "variabilidad": np.random.uniform(0, 1, size=num_filas)  # alguna métrica de dispersión
}

# Crear el DataFrame
df = pd.DataFrame(data_simulada)

# Guardar como CSV
df.to_csv("datos_simulados.csv", index=False)

print("CSV 'datos_simulados.csv' creado con éxito con", num_filas, "filas.")
