import numpy as np
import pandas as pd
import os
from bearing import calcular_bearing

# Define las carpetas de entrada y salida
input_folder = "./Trayectorias/anomalias-v2"
output_folder = "./Trayectorias/anomalias-v2"

# Crear carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Obtener todos los archivos CSV en la carpeta
csv_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.csv')])

# Procesar cada archivo CSV
for file in csv_files:
    input_path = os.path.join(input_folder, file)
    df = pd.read_csv(input_path)

    # Añadir las nuevas columnas
    df['Latitude_2'] = np.nan
    df['Longitude_2'] = np.nan
    df['Time_2'] = None
    df['Bearing'] = np.nan

    # Para cada Trajectory_ID
    trajectory_ids = df['Trajectory_ID'].unique()

    for id in trajectory_ids:
        indices = df[df['Trajectory_ID'] == id].index
        for i in range(len(indices) - 1):
            idx1, idx2 = indices[i], indices[i + 1]
            lat1, lon1 = df.at[idx1, 'Latitude'], df.at[idx1, 'Longitude']
            lat2, lon2 = df.at[idx2, 'Latitude'], df.at[idx2, 'Longitude']
            time_2 = df.at[idx2, 'Time_1']
            bearing = calcular_bearing(lat1, lon1, lat2, lon2)

            df.at[idx1, 'Latitude_2'] = lat2
            df.at[idx1, 'Longitude_2'] = lon2
            df.at[idx1, 'Time_2'] = time_2
            df.at[idx1, 'Bearing'] = bearing

    # Reordenar las columnas
    column_order = ['Trajectory_ID', 'Order', 'Time_1', 'Latitude', 'Longitude', 'Time_2', 'Latitude_2', 'Longitude_2', 'Bearing', 'Type']
    df = df[column_order]

    # Crear el nombre del archivo de salida
    file_number = file.split('.')[0]  # Extraer el número del nombre
    output_filename = f"{file_number}_modificado.csv"
    output_path = os.path.join(output_folder, output_filename)

    # Guardar el DataFrame procesado
    df.to_csv(output_path, index=False)

    print(f"Procesado: {file}")

print("Todos los archivos han sido procesados correctamente.")