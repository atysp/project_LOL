import pandas as pd
from pylol import LolWatcher
import time
import json
import pickle
import os

def extract_challenge_data(match_data, participant_index, challenge_key, default_value=None):
    try:
        return match_data["info"]["participants"][participant_index]["challenges"][challenge_key]
    except KeyError:
        return default_value

def extract_timeline_data(match_data_timeline, participant_index, frame_number, data_key, default_value=None):
    try:
        return match_data_timeline["info"]["frames"][frame_number]["participantFrames"][str(participant_index + 1)][data_key]
    except KeyError:
        return default_value

def scrapping_match_id(lol_watcher, summoner_info, match_id, columns):

    match_id_data = lol_watcher.match.by_match_id(region="europe", match_id=match_id)
    match_id_data_timeline = lol_watcher.match.timeline_by_match_id(region="europe", match_id=match_id)

    # Retrieve the index of the participant player
    participant_index = match_id_data["metadata"]["participants"].index(summoner_info["puuid"])

    # Extract challenge data with default values if not available
    killParticipation = extract_challenge_data(match_id_data, participant_index, "killParticipation")
    teamDamagePercentage = extract_challenge_data(match_id_data, participant_index, "teamDamagePercentage")
    
    # Extract timeline data with default values if not available
    try:
        goldDiffAt10 = match_id_data_timeline["info"]["frames"][10]["participantFrames"][str(participant_index+1)]['totalGold'] - match_id_data_timeline["info"]["frames"][10]["participantFrames"][str((participant_index+1+5)%10)]['totalGold']# on fait +1 car index de 0 à 9 et participant de 1 à 10:
        expDiffAt10 = match_id_data_timeline["info"]["frames"][10]["participantFrames"][str(participant_index+1)]['xp'] - match_id_data_timeline["info"]["frames"][10]["participantFrames"][str((participant_index+1+5)%10)]['xp']
        csDiffAt10 = match_id_data_timeline["info"]["frames"][10]["participantFrames"][str(participant_index+1)]['jungleMinionsKilled'] + match_id_data_timeline["info"]["frames"][10]["participantFrames"][str(participant_index+1)]['minionsKilled'] - (match_id_data_timeline["info"]["frames"][10]["participantFrames"][str((participant_index+1+5)%10)]['jungleMinionsKilled'] + match_id_data_timeline["info"]["frames"][10]["participantFrames"][str((participant_index+1+5)%10)]['minionsKilled'])
    except:
        goldDiffAt10 = None
        expDiffAt10 = None
        csDiffAt10 = None
    try:
        goldDiffAt15 = match_id_data_timeline["info"]["frames"][15]["participantFrames"][str(participant_index+1)]['totalGold'] - match_id_data_timeline["info"]["frames"][15]["participantFrames"][str((participant_index+1+5)%10)]['totalGold']
        expDiffAt15 = match_id_data_timeline["info"]["frames"][15]["participantFrames"][str(participant_index+1)]['xp'] - match_id_data_timeline["info"]["frames"][15]["participantFrames"][str((participant_index+1+5)%10)]['exp']
        csDiffAt15 = match_id_data_timeline["info"]["frames"][15]["participantFrames"][str(participant_index+1)]['jungleMinionsKilled'] + match_id_data_timeline["info"]["frames"][15]["participantFrames"][str(participant_index+1)]['minionsKilled'] - (match_id_data_timeline["info"]["frames"][15]["participantFrames"][str((participant_index+1+5)%10)]['jungleMinionsKilled'] + match_id_data_timeline["info"]["frames"][15]["participantFrames"][str((participant_index+1+5)%10)]['minionsKilled'])
    except:
        goldDiffAt15 = None
        expDiffAt15 = None
        csDiffAt15 = None

    data= [
        [
        match_id_data["metadata"]["matchId"],
        ", ".join(match_id_data["metadata"]["participants"]),
        match_id_data["info"]["platformId"],
        match_id_data["info"]["queueId"],
        match_id_data["info"]["gameDuration"],
        match_id_data["info"]["gameVersion"],
        match_id_data["info"]["mapId"],
        match_id_data["info"]["participants"][participant_index]["puuid"],
        match_id_data["info"]["participants"][participant_index]["summonerName"],
        match_id_data["info"]["participants"][participant_index]["teamId"],
        match_id_data["info"]["participants"][participant_index]["win"],
        match_id_data["info"]["participants"][participant_index]["individualPosition"],
        match_id_data["info"]["participants"][participant_index]["championName"],
        match_id_data["info"]["participants"][participant_index]["champExperience"],

        ## INDIVIDUAL PERFORMANCE
        match_id_data["info"]["participants"][participant_index]["kills"],
        match_id_data["info"]["participants"][participant_index]["assists"],
        match_id_data["info"]["participants"][participant_index]["deaths"],
        match_id_data["info"]["participants"][participant_index]["challenges"]["kda"],
        killParticipation,
        match_id_data["info"]["participants"][participant_index]["challenges"]["damagePerMinute"],
        match_id_data["info"]["participants"][participant_index]["totalMinionsKilled"],
        match_id_data["info"]["participants"][participant_index]["neutralMinionsKilled"],
        match_id_data["info"]["participants"][participant_index]["challenges"]["goldPerMinute"],
        goldDiffAt10,
        goldDiffAt15,
        expDiffAt10,
        expDiffAt15,
        csDiffAt10,
        csDiffAt15,
        ### can be add
        match_id_data["info"]["participants"][participant_index]["challenges"]["soloKills"],
        match_id_data["info"]["participants"][participant_index]["totalTimeCCDealt"],
        match_id_data["info"]["participants"][participant_index]["timeCCingOthers"],
        match_id_data["info"]["participants"][participant_index]["challenges"]["enemyChampionImmobilizations"],
        teamDamagePercentage,
        match_id_data["info"]["participants"][participant_index]["challenges"]["damageTakenOnTeamPercentage"],
        match_id_data["info"]["participants"][participant_index]["totalHeal"],
        match_id_data["info"]["participants"][participant_index]["totalDamageDealtToChampions"],

        ##### Mechanical skills
        # match_id_data["info"]["participants"][participant_index]["totalTimeCCDealt"],
        # match_id_data["info"]["participants"][participant_index]["timeCCingOthers"]
        # match_id_data["info"]["participants"][participant_index]["challenges"]["enemyChampionImmobilizations"]
        # match_id_data["info"]["participants"][participant_index]["challenges"]['dodgeSkillShotsSmallWindow']
        # match_id_data["info"]["participants"][participant_index]["challenges"]['quickCleanse']
        # match_id_data["info"]["participants"][participant_index]["challenges"]['landSkillShotsEarlyGame']
        # match_id_data["info"]["participants"][participant_index]["challenges"]['saveAllyFromDeath']
        # match_id_data["info"]["participants"][participant_index]["challenges"]['skillshotsDodged']
        # match_id_data["info"]["participants"][participant_index]["challenges"]['skillshotsHit']

        ##### Aggressivity
        # match_id_data["info"]["participants"][participant_index]["challenges"]['pickKillWithAlly']
        # match_id_data["info"]["participants"][participant_index]["challenges"]['multikillsAfterAggressiveFlash']
        # match_id_data["info"]["participants"][participant_index]["challenges"]['killsNearEnemyTurret']
        # match_id_data["info"]["participants"][participant_index]["challenges"]['killsOnOtherLanesEarlyJungleAsLaner']
        # match_id_data["info"]["participants"][participant_index]["challenges"]['takedownsAfterGainingLevelAdvantage']
        # match_id_data["info"]["participants"][participant_index]["challenges"]['takedownsFirstXMinutes']


        ## MAP AWARNESS
        match_id_data["info"]["participants"][participant_index]["challenges"]["visionScorePerMinute"],
        match_id_data["info"]["participants"][participant_index]["wardsPlaced"],
        match_id_data["info"]["participants"][participant_index]["challenges"]["controlWardsPlaced"],
        match_id_data["info"]["participants"][participant_index]["challenges"]["stealthWardsPlaced"],
        match_id_data["info"]["participants"][participant_index]["challenges"]["wardsGuarded"],
        match_id_data["info"]["participants"][participant_index]["challenges"]["wardTakedowns"],

        ## Objective and Strategy
        match_id_data["info"]["participants"][participant_index]["challenges"]["dragonTakedowns"],
        match_id_data["info"]["participants"][participant_index]["challenges"]["baronTakedowns"],
        match_id_data["info"]["participants"][participant_index]["challenges"]["riftHeraldTakedowns"],
        match_id_data["info"]["participants"][participant_index]["turretTakedowns"],
        match_id_data["info"]["participants"][participant_index]["inhibitorTakedowns"],
        ###can be add
        match_id_data["info"]["participants"][participant_index]["damageDealtToBuildings"],
        match_id_data["info"]["participants"][participant_index]["damageDealtToObjectives"],
        match_id_data["info"]["participants"][participant_index]["damageDealtToTurrets"],
        match_id_data["info"]["participants"][participant_index]["firstTowerAssist"],
        match_id_data["info"]["participants"][participant_index]["firstTowerKill"],
        match_id_data["info"]["participants"][participant_index]["challenges"]['teamElderDragonKills'],
        match_id_data["info"]["participants"][participant_index]["challenges"]['turretPlatesTaken'],

        ## Communication and Cooperation
        match_id_data["info"]["participants"][participant_index].get("onMyWayPings", None),
        match_id_data["info"]["participants"][participant_index].get("enemyMissingPings", None),
        ### can be add
        match_id_data["info"]["participants"][participant_index].get("allInPings",None), # get pour éviter les erreurs
        match_id_data["info"]["participants"][participant_index].get("assistMePings", None),
        match_id_data["info"]["participants"][participant_index].get("baitPings", None),
        match_id_data["info"]["participants"][participant_index].get("basicPings", None),
        match_id_data["info"]["participants"][participant_index].get("commandPings", None),
        match_id_data["info"]["participants"][participant_index].get("dangerPings", None),
        match_id_data["info"]["participants"][participant_index].get("getBackPings", None),
        match_id_data["info"]["participants"][participant_index].get("holdPings", None),
        match_id_data["info"]["participants"][participant_index].get("needVisionPings", None),
        match_id_data["info"]["participants"][participant_index].get("pushPings", None),
        match_id_data["info"]["participants"][participant_index].get("visionClearedPings", None),
        match_id_data["info"]["participants"][participant_index].get("enemyVisionPings", None),

        ## Ennemy Team stats
        match_id_data["info"]["participants"][(participant_index+5)%10]['kills'] + match_id_data["info"]["participants"][(participant_index+6)%10]['kills'] + match_id_data["info"]["participants"][(participant_index+7)%10]['kills'] + match_id_data["info"]["participants"][(participant_index+8)%10]['kills']  + match_id_data["info"]["participants"][(participant_index+9)%10]['kills'],
        match_id_data["info"]["participants"][(participant_index+5)%10]['deaths'] + match_id_data["info"]["participants"][(participant_index+6)%10]['deaths'] + match_id_data["info"]["participants"][(participant_index+7)%10]['deaths'] + match_id_data["info"]["participants"][(participant_index+8)%10]['deaths']  + match_id_data["info"]["participants"][(participant_index+9)%10]['deaths'],
        match_id_data["info"]["participants"][(participant_index+5)%10]['goldEarned'] + match_id_data["info"]["participants"][(participant_index+6)%10]['goldEarned'] + match_id_data["info"]["participants"][(participant_index+7)%10]['goldEarned'] + match_id_data["info"]["participants"][(participant_index+8)%10]['goldEarned']  + match_id_data["info"]["participants"][(participant_index+9)%10]['goldEarned'],
        match_id_data["info"]["participants"][(participant_index+5)%10]['wardsPlaced'] + match_id_data["info"]["participants"][(participant_index+6)%10]['wardsPlaced'] + match_id_data["info"]["participants"][(participant_index+7)%10]['wardsPlaced'] + match_id_data["info"]["participants"][(participant_index+8)%10]['wardsPlaced']  + match_id_data["info"]["participants"][(participant_index+9)%10]['wardsPlaced'],
        match_id_data["info"]["participants"][(participant_index+5)%10]["champExperience"] + match_id_data["info"]["participants"][(participant_index+6)%10]['champExperience'] + match_id_data["info"]["participants"][(participant_index+7)%10]['champExperience'] + match_id_data["info"]["participants"][(participant_index+8)%10]['champExperience']  + match_id_data["info"]["participants"][(participant_index+9)%10]['champExperience'],
        match_id_data["info"]["participants"][(participant_index+5)%10]["totalDamageDealtToChampions"] + match_id_data["info"]["participants"][(participant_index+6)%10]['totalDamageDealtToChampions'] + match_id_data["info"]["participants"][(participant_index+7)%10]['totalDamageDealtToChampions'] + match_id_data["info"]["participants"][(participant_index+8)%10]['totalDamageDealtToChampions']  + match_id_data["info"]["participants"][(participant_index+9)%10]["totalDamageDealtToChampions"],
        ]
    ]
    
    df = pd.DataFrame(columns=columns, data=data)
    return df

def scrapping(api_key, queue_id, summoner_name, columns, n):

    print(f"On va scrapper les {n*100} derniers matchs de {summoner_name} :")
    print()

    # define the api reference
    lol_watcher = LolWatcher(
        api_key=api_key
    )

    # get summoner informations
    summoner_info = lol_watcher.summoner.by_summoner_name(
        region="euw1",
        summoner_name=summoner_name
    )

    lol_df = pd.DataFrame(columns=columns)

    match_id_list = []

    for i in range (0,n*100,100):

        print(f"Etape numéro {(i//100+1)} sur {n}")

        match_list = lol_watcher.match.by_puuid(
            region="europe",
            encrypted_puuid=summoner_info["puuid"],
            queue_id=queue_id,
            start=i,
            count=100)
        
        lol_df_inter = pd.DataFrame(
            columns=columns)
                
        j=0
        for match_id in match_list:
            time.sleep(2) # on peut essayer de diminuer le time.sleep à 1.2 = 120/100 (100 requetes en 2 minutes)
            print(f"match_id n°{j}: {match_id}") 

            df_add = scrapping_match_id(lol_watcher, summoner_info, match_id, columns)
            lol_df_inter = pd.concat([lol_df_inter,df_add])
            lol_df_inter = lol_df_inter.convert_dtypes()
            j+=1

        # Ajouter le contenu de lol_df au DataFrame initial
        lol_df = pd.concat([lol_df, lol_df_inter], ignore_index=True)
    return lol_df

def main():

    api_key = "RGAPI-d50d98e1-8a6e-4ce0-a325-500118b5dd4c"
    queue_id = 420

    # GW : ["Badlulu00", "GW Villager", "ayekasia", "Practice", "zrh2"]
    # KC : ["KC Gaulois", "Cz6 Cinkrof", "Shïru", "KC NEXT ADKING", "Targamas"]
    # Vit : ["Scarface", "Daglas", "Czajek", "Neon", "Jactroll"]]
    # Frkl : ["Nevaray, tureoul, "Win Or Go Afk", "theredstonebest", "atysp" ]
    team = "GW"

    summoner_names = []
    with open('/Users/atysp/Desktop/Avisia/projet_lol/drafting/dico_summoner_names_lfl.pkl', 'rb') as f:
        dico = pickle.load(f)

    import re

    def extract_word_before_comma(text):
        # Utiliser une expression régulière pour trouver un mot avant une virgule
            
        match = re.search(r'\b([^\s,]+)(?:,\s*|\s*,)', text)
        
        if match:
            word = match.group(1)
            return word
        else:
            return text

    for key in dico.keys():
            sub_dico = dico[key]
            for clef in sub_dico.keys():
                if clef=='EUW':
                    pseudo = extract_word_before_comma(sub_dico[clef])
                    print(pseudo)
                    summoner_names.append(pseudo)

    n=1
    columns=[
    "matchId",
    "participants",
    "platformId",
    "queueId",
    "gameDuration",
    "gameVersion",
    "mapId",
    "puuid",
    "summonerName",
    "teamId",
    "win",
    "individualPosition",
    "championName",
    "champExperience",

    "kills",
    "assists",
    "deaths",
    "kda",
    "killParticipation",
    "damagePerMinute",
    "totalMinionsKilled",
    "neutralMinionsKilled",
    "goldPerMinute",
    "goldDiffAt10",
    "goldDiffAt15",
    "expDiffAt10",
    "expDiffAt15",
    "csDiffAt10",
    "csDiffAt15",
    "soloKills",
    "totalTimeCCDealt",
    "timeCCingOthers",
    "enemyChampionImmobilizations",
    "teamDamagePercentage",
    "damageTakenOnTeamPercentage",
    "totalHeal",
    "totalDamageDealtToChampions",

    "visionScorePerMinute",
    "wardsPlaced",
    "controlWardsPlaced",
    "stealthWardsPlaced",
    "wardsGuarded",
    "wardTakedowns",

    "dragonTakedowns",
    "baronTakedowns",
    "riftHeraldTakedowns",
    "turretTakedowns",
    "inhibitorTakedowns",
    "damageDealtToBuildings",
    "damageDealtToObjectives",
    "damageDealtToTurrets",
    "firstTowerAssist",
    "firstTowerKill",
    'teamElderDragonKills',
    'turretPlatesTaken',

    "onMyWayPings",
    "enemyMissingPings",
    "allInPings",
    "assistMePings",
    "baitPings",
    "basicPings",
    "commandPings",
    "dangerPings",
    "getBackPings",
    "holdPings",
    "needVisionPings",
    "pushPings",
    "visionClearedPings",
    "enemyVisionPings",

    "ennemyTeamKills",
    "ennemyTeamDeaths",
    "ennemyTeamGolds",
    "ennemyTeamWardPlaced",
    "ennemyTeamTotalLvl",
    "ennemyTeamDamages",
    ]

    for summoner_name in summoner_names :
        lol_df = scrapping(api_key, queue_id, summoner_name, columns, n)
        print("Bravo it's done")
        print(lol_df.shape)

        # os.makedirs(team, exist_ok=True)
        # Sauvegarder le nouveau DataFrame dans le même fichier pickle
        with open(f'lol_df_{summoner_name}.pkl', 'wb') as f:
            pickle.dump(lol_df, f)

if __name__ == "__main__":
    main()

    #     # Création d'un dictionnaire avec les clés et les valeurs associées
    # donnees = {
    # "matchId": match_id_data["metadata"]["matchId"],
    # "participants": ", ".join(match_id_data["metadata"]["participants"]),
    # "platformId": match_id_data["info"]["platformId"],
    # "queueId": match_id_data["info"]["queueId"],
    # "gameDuration": match_id_data["info"]["gameDuration"],
    # "gameVersion": match_id_data["info"]["gameVersion"],
    # "mapId": match_id_data["info"]["mapId"],
    # "puuid": match_id_data["info"]["participants"][participant_index]["puuid"],
    # "summonerName": match_id_data["info"]["participants"][participant_index]["summonerName"],
    # "teamId": match_id_data["info"]["participants"][participant_index]["teamId"],
    # "win": match_id_data["info"]["participants"][participant_index]["win"],
    # "individualPosition": match_id_data["info"]["participants"][participant_index]["individualPosition"],
    # "championName": match_id_data["info"]["participants"][participant_index]["championName"],
    
    # "kills": match_id_data["info"]["participants"][participant_index]["kills"],
    # "assists": match_id_data["info"]["participants"][participant_index]["assists"],
    # "deaths": match_id_data["info"]["participants"][participant_index]["deaths"],
    # "kda": match_id_data["info"]["participants"][participant_index]["challenges"]["kda"],
    # "killParticipation": killParticipation,
    # "damagePerMinute": match_id_data["info"]["participants"][participant_index]["challenges"]["damagePerMinute"],
    # "totalMinionsKilled": match_id_data["info"]["participants"][participant_index]["totalMinionsKilled"],
    # "neutralMinionsKilled": match_id_data["info"]["participants"][participant_index]["neutralMinionsKilled"],
    # "goldPerMinute": match_id_data["info"]["participants"][participant_index]["challenges"]["goldPerMinute"],
    # "goldDiffAt10": goldDiffAt10,
    # "goldDiffAt15": goldDiffAt15,
    # "expDiffAt10": expDiffAt10,
    # "expDiffAt15": expDiffAt15,
    # "csDiffAt10": csDiffAt10,
    # "csDiffAt15": csDiffAt15,
    
    # "soloKills": match_id_data["info"]["participants"][participant_index]["challenges"]["soloKills"],
    # "totalTimeCCDealt": match_id_data["info"]["participants"][participant_index]["totalTimeCCDealt"],
    # "timeCCingOthers": match_id_data["info"]["participants"][participant_index]["timeCCingOthers"],
    # "enemyChampionImmobilizations": match_id_data["info"]["participants"][participant_index]["challenges"]["enemyChampionImmobilizations"],
    # "teamDamagePercentage": teamDamagePercentage,
    # "damageTakenOnTeamPercentage": match_id_data["info"]["participants"][participant_index]["challenges"]["damageTakenOnTeamPercentage"],
    
    # "visionScorePerMinute": match_id_data["info"]["participants"][participant_index]["challenges"]["visionScorePerMinute"],
    # "wardsPlaced": match_id_data["info"]["participants"][participant_index]["wardsPlaced"],
    # "controlWardsPlaced": match_id_data["info"]["participants"][participant_index]["challenges"]["controlWardsPlaced"],
    # "stealthWardsPlaced": match_id_data["info"]["participants"][participant_index]["challenges"]["stealthWardsPlaced"],
    # "wardsGuarded": match_id_data["info"]["participants"][participant_index]["challenges"]["wardsGuarded"],
    # "wardTakedowns": match_id_data["info"]["participants"][participant_index]["challenges"]["wardTakedowns"],
    
    # "dragonTakedowns": match_id_data["info"]["participants"][participant_index]["challenges"]["dragonTakedowns"],
    # "baronTakedowns": match_id_data["info"]["participants"][participant_index]["challenges"]["baronTakedowns"],
    # "riftHeraldTakedowns": match_id_data["info"]["participants"][participant_index]["challenges"]["riftHeraldTakedowns"],
    # "turretTakedowns": match_id_data["info"]["participants"][participant_index]["turretTakedowns"],
    # "inhibitorTakedowns": match_id_data["info"]["participants"][participant_index]["inhibitorTakedowns"],
    
    # "damageDealtToBuildings": match_id_data["info"]["participants"][participant_index]["damageDealtToBuildings"],
    # "damageDealtToObjectives": match_id_data["info"]["participants"][participant_index]["damageDealtToObjectives"],
    # "damageDealtToTurrets": match_id_data["info"]["participants"][participant_index]["damageDealtToTurrets"],
    # "firstTowerAssist": match_id_data["info"]["participants"][participant_index]["firstTowerAssist"],
    # "firstTowerKill": match_id_data["info"]["participants"][participant_index]["firstTowerKill"],
    
    # "onMyWayPings": match_id_data["info"]["participants"][participant_index].get("onMyWayPings", None),
    # "enemyMissingPings": match_id_data["info"]["participants"][participant_index].get("enemyMissingPings", None),
    # "allInPings": match_id_data["info"]["participants"][participant_index].get("allInPings", None),
    # "assistMePings": match_id_data["info"]["participants"][participant_index].get("assistMePings", None),
    # "baitPings": match_id_data["info"]["participants"][participant_index].get("baitPings", None),
    # "basicPings": match_id_data["info"]["participants"][participant_index].get("basicPings", None),
    # "commandPings": match_id_data["info"]["participants"][participant_index].get("commandPings", None),
    # "dangerPings": match_id_data["info"]["participants"][participant_index].get("dangerPings", None),
    # "getBackPings": match_id_data["info"]["participants"][participant_index].get("getBackPings", None),
    # "holdPings": match_id_data["info"]["participants"][participant_index].get("holdPings", None),
    # "needVisionPings": match_id_data["info"]["participants"][participant_index].get("needVisionPings", None),
    # "pushPings": match_id_data["info"]["participants"][participant_index].get("pushPings", None),
    # "visionClearedPings": match_id_data["info"]["participants"][participant_index].get("visionClearedPings", None),
    # "enemyVisionPings": match_id_data["info"]["participants"][participant_index].get("enemyVisionPings", None),
    # }
