import numpy as np
import pandas as pd
from bearing import calcular_bearing

df_path = "./Trayectorias/Tipos_de_barcos/Cargo_modificado.csv"
df = pd.read_csv(df_path)

print(df.head())