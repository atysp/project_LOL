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
        
        extract_challenge_data(match_id_data, participant_index, "kda"),
        killParticipation,
        extract_challenge_data(match_id_data, participant_index, "DamagePerMinute"),
        match_id_data["info"]["participants"][participant_index]["totalMinionsKilled"],
        match_id_data["info"]["participants"][participant_index]["neutralMinionsKilled"],
        extract_challenge_data(match_id_data, participant_index, "goldPerMinute"),
        goldDiffAt10,
        goldDiffAt15,
        expDiffAt10,
        expDiffAt15,
        csDiffAt10,
        csDiffAt15,
        ### can be add
        extract_challenge_data(match_id_data, participant_index, "soloKills"),
        match_id_data["info"]["participants"][participant_index]["totalTimeCCDealt"],
        match_id_data["info"]["participants"][participant_index]["timeCCingOthers"],
        extract_challenge_data(match_id_data, participant_index, "enemyChampionImmobilizations"),
        teamDamagePercentage,
        extract_challenge_data(match_id_data, participant_index, "damageTakenOnTeamPercentage"),
        match_id_data["info"]["participants"][participant_index]["totalHeal"],
        match_id_data["info"]["participants"][participant_index]["totalDamageDealtToChampions"],

        ##### Mechanical skills
        # extract_challenge_data(match_id_data, participant_index, "enemyChampionImmobilizations"),
        # extract_challenge_data(match_id_data, participant_index, "dodgeSkillShotsSmallWindow"),
        # extract_challenge_data(match_id_data, participant_index, "quickCleanse"),
        # extract_challenge_data(match_id_data, participant_index, "landSkillShotsEarlyGame"),
        # extract_challenge_data(match_id_data, participant_index, "saveAllyFromDeath"),
        # extract_challenge_data(match_id_data, participant_index, "skillshotsDodged"),
        # extract_challenge_data(match_id_data, participant_index, "skillshotsHit"),

        ##### Aggressivity
        # extract_challenge_data(match_id_data, participant_index, "pickKillWithAlly"),
        # extract_challenge_data(match_id_data, participant_index, "multikillsAfterAggressiveFlash"),
        # extract_challenge_data(match_id_data, participant_index, "killsNearEnemyTurret"),
        # extract_challenge_data(match_id_data, participant_index, "killsOnOtherLanesEarlyJungleAsLaner"),
        # extract_challenge_data(match_id_data, participant_index, "takedownsAfterGainingLevelAdvantage"),
        # extract_challenge_data(match_id_data, participant_index, "takedownsFirstXMinutes"),

        ## MAP AWARNESS
        extract_challenge_data(match_id_data, participant_index, "visionScorePerMinute"),
        match_id_data["info"]["participants"][participant_index]["wardsPlaced"],
        extract_challenge_data(match_id_data, participant_index, "controlWardsPlaced"),
        extract_challenge_data(match_id_data, participant_index, "stealthWardsPlaced"),
        extract_challenge_data(match_id_data, participant_index, "wardsGuarded"),
        extract_challenge_data(match_id_data, participant_index, "wardTakedowns"),

        # Objective and Strategy
        extract_challenge_data(match_id_data, participant_index, "dragonTakedowns"),
        extract_challenge_data(match_id_data, participant_index, "baronTakedowns"),
        extract_challenge_data(match_id_data, participant_index, "riftHeraldTakedowns"),
        match_id_data["info"]["participants"][participant_index]["turretTakedowns"],
        match_id_data["info"]["participants"][participant_index]["inhibitorTakedowns"],
        ###can be add
        match_id_data["info"]["participants"][participant_index]["damageDealtToBuildings"],
        match_id_data["info"]["participants"][participant_index]["damageDealtToObjectives"],
        match_id_data["info"]["participants"][participant_index]["damageDealtToTurrets"],
        match_id_data["info"]["participants"][participant_index]["firstTowerAssist"],
        match_id_data["info"]["participants"][participant_index]["firstTowerKill"],
        extract_challenge_data(match_id_data, participant_index, "teamElderDragonKills"),
        extract_challenge_data(match_id_data, participant_index, "turretPlatesTaken"),

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
    try:
        summoner_info = lol_watcher.summoner.by_summoner_name(region="euw1", summoner_name=summoner_name)
    except ValueError :
        data=[]
        lol_df = pd.DataFrame(data, columns=columns)
        return lol_df

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

    # Chemin absolu du dossier courant
    chemin_fichier_python = os.path.abspath(__file__)
    chemin_src = os.path.dirname(chemin_fichier_python)
    chemin_pylol = os.path.dirname(chemin_src)
    chemin_scouting = os.path.dirname(chemin_pylol)

    # GW : ["Badlulu00", "GW Villager", "ayekasia", "Practice", "zrh2"]
    # KC : ["KC Gaulois", "Cz6 Cinkrof", "Shïru", "KC NEXT ADKING", "Targamas"]
    # Vit : ["Scarface", "Daglas", "Czajek", "Neon", "Jactroll"]

    api_key = "RGAPI-e1b22e12-3f40-46a0-b207-b6ce9f6f1d0a"
    queue_id = 420

    team = "KC"
    summoner_names = ["KC Gaulois", "Cz6 Cinkrof", "Shïru", "KC NEXT ADKING", "Targamas"]

    ## BONUS : avoir les summoner names des joueurs pro par ligue : BONUS 
    # ligue = "lfl"
    # summoner_names=[]
    # with open(chemin_scouting + f"/datas/summoner_names/dico_summoner_names_{ligue}.pkl", 'rb') as f:
    #     dico = pickle.load(f)
    # import re
    # def extract_word_before_comma(text):
    #     # Utiliser une expression régulière pour trouver un mot avant une virgule     
    #     match = re.search(r'\b([^\s,]+)(?:,\s*|\s*,)', text)
        
    #     if match:
    #         word = match.group(1)
    #         return word
    #     else:
    #         return text

    # for key in dico.keys():
    #         sub_dico = dico[key]
    #         for clef in sub_dico.keys():
    #             if clef=='EUW':
    #                 pseudo = extract_word_before_comma(sub_dico[clef])
    #                 print(pseudo)
    #                 summoner_names.append(pseudo)
    # print(f"La liste de summoner names est : {summoner_names}")
    # print()

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

        # Chemin absolu du dossier courant
        chemin_fichier_python = os.path.abspath(__file__)
        chemin_src = os.path.dirname(chemin_fichier_python)
        chemin_pylol = os.path.dirname(chemin_src)
        chemin_scouting = os.path.dirname(chemin_pylol)

        chemin_equipe = chemin_scouting + "/datas/matches/equipes/" + team
        os.makedirs(chemin_equipe, exist_ok=True)
        
        chemin_dataset = chemin_scouting + "/datas/matches/equipes/" + team + f'/lol_df_{summoner_name}.pkl'
        # Sauvegarder le nouveau DataFrame dans le fichier pickle
        with open(chemin_dataset, 'wb') as f:
            pickle.dump(lol_df, f)

    # # BONUS : avoir les summoner names des joueurs pro ligue: BONUS 
    # ligue = ligue.upper()
    # for summoner_name in summoner_names :

    #     lol_df = scrapping(api_key, queue_id, summoner_name, columns, n)

    #     print("Bravo it's done")
    #     print(lol_df.shape)
    #     chemin_ligue = chemin_scouting + "/datas/matches/ligues/" + ligue
    #     os.makedirs(chemin_ligue, exist_ok=True)
        
    #     chemin_dataset = chemin_scouting + "/datas/matches/ligues/" + ligue + f'/lol_df_{summoner_name}.pkl'
    #     # Sauvegarder le nouveau DataFrame dans le fichier pickle
    #     with open(chemin_dataset, 'wb') as f:
    #         pickle.dump(lol_df, f)

if __name__ == "__main__":
    main()
