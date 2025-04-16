import numpy as np
import pandas as pd
from bearing import calcular_bearing

df_path = "./Trayectorias/trajectories_dataset_ordenado_v4.csv"
df = pd.read_csv(df_path)

types = df['Type'].unique()

for type_value in types:

    df_type = df[df['Type'] == type_value].copy()
    
    df_type['Latitude_2'] = np.nan
    df_type['Longitude_2'] = np.nan
    df_type['Bearing'] = np.nan
    
    trajectory_ids = df_type['Trajectory_ID'].unique()
    
    for id in trajectory_ids:
        indices = df_type[df_type['Trajectory_ID'] == id].index
        for i in range(len(indices) - 1):
            idx1, idx2 = indices[i], indices[i + 1]
            lat1, lon1 = df_type.at[idx1, 'Latitude'], df_type.at[idx1, 'Longitude']
            lat2, lon2 = df_type.at[idx2, 'Latitude'], df_type.at[idx2, 'Longitude']
            bearing = calcular_bearing(lat1, lon1, lat2, lon2)
            
            df_type.at[idx1, 'Latitude_2'] = lat2
            df_type.at[idx1, 'Longitude_2'] = lon2
            df_type.at[idx1, 'Bearing'] = bearing
    
    column_order = ['Trajectory_ID', 'Order', 'Latitude', 'Longitude', 'Latitude_2', 'Longitude_2', 'Bearing', 'Type']
    df_type = df_type[column_order]
    
    file_name = f"./Trayectorias/Tipos_de_barcos/v4/{type_value}_modificado_v4.csv"
    df_type.to_csv(file_name, index=False)