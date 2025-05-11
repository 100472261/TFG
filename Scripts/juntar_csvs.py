import os
import pandas as pd

# Define el path a la carpeta que quieres procesar
folder_path = "./Trayectorias/Tipos_de_barcos/v5/(90-99) Other Type"  # Cambia esto si quieres otra carpeta
output_filename = "all_modificado_v5.csv"  # Nombre del archivo final combinado

# Obtiene la lista de archivos que terminan en '_modificado_v5.csv'
csv_files = [f for f in os.listdir(folder_path) if f.endswith('_modificado_v5.csv')]

# Ordena los archivos numéricamente basado en el número antes de '_modificado_v5'
csv_files_sorted = sorted(csv_files, key=lambda x: int(x.split('_')[0]))

# Lista para ir guardando los dataframes
dataframes = []

# Recorre cada archivo CSV y cárgalo
for csv_file in csv_files_sorted:
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path)
    dataframes.append(df)

# Une todos los dataframes en uno solo
merged_df = pd.concat(dataframes, ignore_index=True)

# Guarda el dataframe combinado en un nuevo CSV
output_path = os.path.join(folder_path, output_filename)
merged_df.to_csv(output_path, index=False)

print(f"Todos los archivos han sido combinados exitosamente en: {output_path}")