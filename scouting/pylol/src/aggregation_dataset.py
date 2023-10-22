# Pour parcourir les fichiers pickle dans un dossier, agréger les données en fusionnant les datasets et supprimer les lignes redondantes,
import os
import pandas as pd

def aggregate_datasets(folder_path):
    # Créer une liste pour stocker les DataFrames
    dataframes = []

    # Parcourir tous les fichiers dans le dossier
    for filename in os.listdir(folder_path):
        if filename.endswith(".pkl"):
            file_path = os.path.join(folder_path, filename)
            
            # Charger le DataFrame depuis le fichier pickle
            df = pd.read_pickle(file_path)
            # Ajouter le DataFrame à la liste
            dataframes.append(df)

    # Concaténer les DataFrames en un seul DataFrame
    aggregated_df = pd.concat(dataframes, ignore_index=True)

    # Supprimer les lignes redondantes
    aggregated_df.drop_duplicates(inplace=True)

    return aggregated_df

# Exemple d'utilisation de la fonction
folder_path_1 = "/Users/atysp/Desktop/Avisia/projet_lol/scouting/datas/matches/ligues/EMEA"
result_df_1 = aggregate_datasets(folder_path_1)

folder_path_2 = "/Users/atysp/Desktop/Avisia/projet_lol/scouting/datas/matches/ligues/LFL"
result_df_2 = aggregate_datasets(folder_path_2)

folder_path_3 = "/Users/atysp/Desktop/Avisia/projet_lol/scouting/datas/matches/ligues/LCK"
result_df_3 = aggregate_datasets(folder_path_3)

result_df = pd.concat([result_df_1, result_df_2, result_df_3], ignore_index=True)

print(result_df.shape)

