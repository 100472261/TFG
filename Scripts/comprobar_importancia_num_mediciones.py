import pandas as pd

csv1 = pd.read_csv('./Trayectorias/Tipos_de_barcos/longitud_28/(90-99)_modificado_compressed_28_v5_COMPLETO.csv')
csv2 = pd.read_csv('./Trayectorias/Tipos_de_barcos/longitud_8/(90-99)_modificado_compressed_8_v5_COMPLETO.csv')

ids_csv1 = csv1['Trajectory_ID'].unique()

filtered_csv2 = csv2[csv2['Trajectory_ID'].isin(ids_csv1)]

filtered_csv2.to_csv('(90-99)_modificado_compressed_8_v5.csv', index=False)