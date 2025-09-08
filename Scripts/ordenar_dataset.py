import pandas as pd

df = pd.read_csv('./Trayectorias/anomaly_dataset_original_v2.csv')

df_ordenado = df.sort_values(by=['Trajectory_ID', 'timestamp'])

column_order = ['Trajectory_ID', 'timestamp', 'lat', 'lon', 'Anomaly']
df_ordenado = df_ordenado[column_order]

# Añadir el atributo 'Order' para cada Trajectory_ID
df_ordenado['Order'] = df_ordenado.groupby('Trajectory_ID').cumcount()

# Cambiar el nombre de las columnas
df_ordenado = df_ordenado.rename(columns={
    'lat': 'Latitude',
    'lon': 'Longitude',
    'timestamp': 'Time_1',
    'Anomaly': 'Type'
})

# Reordenar columnas para incluir 'Order'
final_columns = ['Trajectory_ID', 'Order', 'Time_1', 'Latitude', 'Longitude', 'Type']
df_ordenado = df_ordenado[final_columns]

df_ordenado.to_csv('./Trayectorias/anomaly_dataset_ordenado_v2.csv', index=False)