import glob
import pandas as pd
from sklearn.model_selection import train_test_split

file_paths = glob.glob('./Trayectorias/Tipos_de_barcos/*_modificado.csv')

dfs = []

for file_path in file_paths:
    df = pd.read_csv(file_path)
    dfs.append(df)

data = dfs[0]

trayectorias = data["Trajectory_ID"].unique()
train, test = train_test_split(trayectorias, test_size=0.2, random_state=42)
train_data = data[data["Trajectory_ID"].isin(train)]
test_data = data[data["Trajectory_ID"].isin(test)]