import pandas as pd       # Para manejar tablas de datos
import numpy as np        # Para cálculos numéricos
from sklearn.preprocessing import StandardScaler  # Para normalizar
from sklearn.cluster import KMeans               # Para agrupar
from sklearn.metrics import pairwise_distances_argmin_min  # Para encontrar el grupo más cercano
import os

if not os.path.exists("datos_simulados.csv"):
    import csv_gen  # Asegúrate de que el CSV esté generado
# Ruta absoluta del script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "datos_simulados.csv")

data = pd.read_csv(csv_path)

variables = ["frecuencia", "tiempo_promedio_sesion", "acciones_totales", "recencia", "variabilidad"]
df = data[variables]

# Normalizar los datos

df = df.fillna(df.median()) # Rellenar valores faltantes con la mediana

# Esto evita que una variable domine a las demás por su escala
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)


#Entrenar el modelo de K-Means n_clusters = numero de grupos / perfiles / clusters, random_state para reproducibilidad es la semilla / seed
kmeans = KMeans(n_clusters=6, random_state=42)
kmeans.fit(df_scaled)

data["grupo"] = kmeans.labels_

centroides = data.groupby("grupo")[variables].mean()

# Ejemplo de cómo encontrar el grupo de un nuevo usuario
nuevo_usuario = pd.DataFrame({
    "frecuencia": [12],
    "tiempo_promedio_sesion": [18],
    "acciones_totales": [177],
    "recencia": [241],
    "variabilidad": [0.3]
})
centroides_scaled = scaler.transform(centroides)
nuevo_usuario_scaled = scaler.transform(nuevo_usuario)
grupo_nuevo_usuario,_ = pairwise_distances_argmin_min(nuevo_usuario_scaled, centroides_scaled)
print(centroides)
print(f"El nuevo usuario pertenece al grupo: {grupo_nuevo_usuario[0]}")
