#Este script separa los tipos de barcos del .csv en diferentes archivos .csv

import pandas as pd

def count_unique_trajectory_ids(input_csv):
    df = pd.read_csv(input_csv)
    unique_ids = df['Trajectory_ID'].nunique()
    print(f"Número de Trajectory_ID únicos: {unique_ids}")

# Ejemplo de uso:
test_csv = "./Trayectorias/Tipos_de_barcos/v5/(90-99) Other Type/all_modificado_v5.csv"
count_unique_trajectory_ids(test_csv)

"""
# Cargar el archivo CSV
df = pd.read_csv('./Trayectorias/trajectories_dataset_ordenado_v5.csv')

# Crear la nueva columna 'Order'
df['Order'] = df.groupby('Trajectory_ID').cumcount()

columnas_ordenadas = ['Trajectory_ID', 'Order', 'Time_1', 'Latitude', 'Longitude', 'Type']
df = df[columnas_ordenadas]

# Guardar el DataFrame actualizado en un nuevo CSV
df.to_csv('./Trayectorias/trajectories_dataset_ordenado_v5.csv', index=False)
"""
"""
def split_csv_by_type(input_csv, output_folder):
    df = pd.read_csv(input_csv)
    
    if 'Type' not in df.columns:
        raise ValueError("La columna 'Type' no se encuentra en el archivo CSV.")
    
    for type_value in df['Type'].unique():
        df_type = df[df['Type'] == type_value]
        output_file = f"{output_folder}/{type_value}.csv"
        df_type.to_csv(output_file, index=False)
        print(f"Archivo generado: {output_file}")


test_csv = "./Trayectorias/trajectories_dataset_ordenado_v5.csv"
output_directory = "./Trayectorias/Tipos_de_barcos/v5"
split_csv_by_type(test_csv, output_directory)
"""
"""
def view_csv_attributes(input_csv):
    df = pd.read_csv(input_csv)
    print("Columnas del archivo CSV:")
    print(df.columns)
    print("\nPrimeras filas del archivo CSV:")
    print(df.head())

# Ejemplo de uso:
test_csv = "./Trayectorias/trajectories_dataset_ordenado_v5.csv"
view_csv_attributes(test_csv)
"""

"""
def find_null_type_rows(input_csv):
    df = pd.read_csv(input_csv)
    null_type_rows = df[df['Type'].isnull()]
    if null_type_rows.empty:
        print("No se encontraron filas con 'Type' nulo.")
    else:
        print("Filas con 'Type' nulo encontradas:")
        print(null_type_rows)

# Ejemplo de uso:
test_csv = "./Trayectorias/trajectories_dataset_ordenado_v5.csv"
find_null_type_rows(test_csv)
"""

"""
def remove_rows_with_type_zero_or_200(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df_filtered = df[(df['Type'] != 0) & (df['Type'] != 200)]
    df_filtered.to_csv(output_csv, index=False)
    print(f"Archivo generado sin filas con 'Type' == 0 o 'Type' == 200: {output_csv}")

# Ejemplo de uso:
test_csv = "./Trayectorias/trajectories_dataset_ordenado_v5.csv"
output_csv = "./Trayectorias/trajectories_dataset_ordenado_v5_ok.csv"
remove_rows_with_type_zero_or_200(test_csv, output_csv)
"""