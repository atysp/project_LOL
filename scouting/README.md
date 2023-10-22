DOCUMENT D'EXPLICATION DU DOSSIER SCOUTING

A. Notebooks

1. analyse_v1.ipynb

BUT:
Sélectionner des variables pertinentes pour créer des méta-indicateurs (KPI) décrivant le style de jeu d'un joueur. 

ANALYSE:
Les KPIs incluent les performances individuelles, la vision et le contrôle de la carte, les objectifs et la stratégie, l'adaptabilité (champions pool), la communication et la coopération. Pour visualiser ces KPIs, des graphiques en forme de radar ont été proposés, permettant une représentation visuelle globale des forces et faiblesses du joueur dans chaque domaine.

2. analyse_v2.ipynb

BUT:
Établir une liste restreinte d'une dizaine de métriques qui reflètent le niveau du joueur dans la partie.

3. analyse_player.ipynb

BUT : 
Déterminer un coefficient de corrélation pour chacune des 11 métriques utilisées en utilisant la corrélation avec la victoire.
Standardiser chaque colonne en soustrayant la moyenne et en divisant par l'écart-type.
Multiplier les valeurs standardisées par le coefficient de corrélation correspondant, puis additionner les valeurs de la ligne et diviser par la somme des corrélations. 

ANALYSE :
Cela donne un nombre qui représente la performance relative du joueur sur la partie.

B. Pylol

1. Creation_table_v2.py

BUT : 
Scrapper les 100*n derniers match d'un joueur à partir de son nom d'invocateur (summoner name).

2. aggregation_dataset.py 

BUT : 
Parcourir les fichiers pickle de données dans un dossier, fusionner les datasets et supprimer les doublons.



















