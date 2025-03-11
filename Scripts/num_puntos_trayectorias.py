import numpy as np
import pandas as pd

if __name__ == "__main__":
    df_path = "./Trayectorias/Tipos_de_barcos/Cargo_modificado.csv"
    df = pd.read_csv(df_path)

    trajectory_ids = df['Trajectory_ID'].unique()

    length_counts = {}

    for id in trajectory_ids:
        count = df[df['Trajectory_ID'] == id].shape[0]
        if count in length_counts:
            length_counts[count].append(id)
        else:
            length_counts[count] = [id]

    for length, ids in sorted(length_counts.items()):
        print(f"### ID's con longitud {length}: {len(ids)} ###")
        print(f"Ejemplo: {ids[0:5]}")
        print()