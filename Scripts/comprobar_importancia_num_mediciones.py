import pandas as pd

csv1 = pd.read_csv('./Trayectorias/Tipos_de_barcos/longitud_28/Tanker_modificado_compressed_28_v2.csv')
csv2 = pd.read_csv('./Trayectorias/Tipos_de_barcos/longitud_8/Tanker_modificado_compressed_8_v2.csv')

ids_csv1 = csv1['Trajectory_ID'].unique()

filtered_csv2 = csv2[csv2['Trajectory_ID'].isin(ids_csv1)]

filtered_csv2.to_csv('Prueba_Tanker.csv', index=False)
