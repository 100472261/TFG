#Este script separa los tipos de barcos del .csv en diferentes archivos .csv

import pandas as pd

def split_csv_by_type(input_csv, output_folder):
    df = pd.read_csv(input_csv)
    
    if 'Type' not in df.columns:
        raise ValueError("La columna 'Type' no se encuentra en el archivo CSV.")
    
    for type_value in df['Type'].unique():
        df_type = df[df['Type'] == type_value]
        output_file = f"{output_folder}/{type_value}.csv"
        df_type.to_csv(output_file, index=False)
        print(f"Archivo generado: {output_file}")

test_csv = "./Trayectorias/trajectories_dataset_ordenado_v4.csv"
output_directory = "./Trayectorias/Tipos_de_barcos/v4"
split_csv_by_type(test_csv, output_directory)