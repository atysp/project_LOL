# Scouting Analysis Documentation

## A. Notebooks

### 1. analyse_v1.ipynb

**Objective:**
Select relevant variables to create meta-indicators (KPIs) describing a player's gameplay style.

**Analysis:**
The KPIs include individual performance, map awareness and control, objectives and strategy, adaptability (champion pool), communication, and cooperation. Radar charts are proposed to visualize these KPIs, allowing for a comprehensive visual representation of a player's strengths and weaknesses in each area.

### 2. analyse_v2.ipynb

**Objective:**
Establish a shortlist of about ten metrics that reflect the player's level in the game.

### 3. analyse_player.ipynb

**Objective:**
Determine a correlation coefficient for each of the 11 metrics used by correlating them with victory. Standardize each column by subtracting the mean and dividing by the standard deviation. Multiply the standardized values by the corresponding correlation coefficient, then sum the values in the row and divide by the sum of correlations.

**Analysis:**
This yields a number representing the player's relative performance in the game.

## B. Pylol

### 1. Creation_table_v2.py

**Objective:**
Scrape the last 100*n matches of a player based on their summoner name.

### 2. aggregation_dataset.py

**Objective:**
Browse the pickle data files in a folder, merge datasets, and remove duplicates.




















