import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #df_path = "./Trayectorias/Tipos_de_barcos/v5/(90-99) Other Type/all_modificado_v5.csv"
    df_path = "./Trayectorias/Anomalias/1_modificado.csv"
    #df_path = "./Trayectorias/Tipos_de_barcos/Cruise_modificado.csv"
    #df_path = "./Trayectorias/Tipos_de_barcos/Fishing_modificado.csv"
    #df_path = "./Trayectorias/Tipos_de_barcos/Tanker_modificado.csv"

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
        print(f"Ejemplos: {[int(id) for id in ids[0:5]]}")
        print()

    # Crear gráfica de barras
    #lengths = sorted(length_counts.keys())
    #counts = [len(length_counts[length]) for length in lengths]

    #plt.figure(figsize=(10, 6))
    #plt.bar(lengths, counts, color='black')
    #plt.xlabel("Longitud de una trayectoria")
    #plt.ylabel("Nº de trayectorias")
    #plt.grid(axis='y', linestyle='--', alpha=0.7)
    #plt.tight_layout()
    #plt.show()