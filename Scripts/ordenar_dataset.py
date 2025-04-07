import pandas as pd

df = pd.read_csv('./Trayectorias/trajectories_dataset_original_v3.csv')

df_ordenado = df.sort_values(by=['Trajectory_ID', 'Order'])

column_order = ['Trajectory_ID', 'Order', 'Latitude', 'Longitude', 'Type']

df_ordenado = df_ordenado[column_order]

df_ordenado.to_csv('./Trayectorias/trajectories_dataset_ordenado_v3.csv', index=False)