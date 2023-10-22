import pandas as pd
from pylol import LolWatcher
import time
import json
import pickle

api_key = "RGAPI-ef23f951-03d5-4da9-909a-b7df8dbead5e"
queue_id = 420

# GW : ["Badlul00", "GW Villager", "ayekasia", "Practice", "zrh2"]
# KC : ["KC Gaulois", "Cz6 Cinkrof", "Shïru", "KC NEXT ADKING", "Targamas"]
# Vit : ["Scarface", "Daglas", "Czajek", "Neon", "Jactroll"]]

summoner_names = ["KC Gaulois", "Cinkrof", "Shïru", "KC NEXT ADKING", "Targamas"]

for summoner_name in summoner_names :

    # define the api reference
    lol_watcher = LolWatcher(
        api_key=api_key
    )

    # get summoner informations
    summoner_info = lol_watcher.summoner.by_summoner_name(
        region="euw1",
        summoner_name=summoner_name
    )

    # define dataframe schema for output
    lol_df = pd.DataFrame(
        columns=[
            "matchId",
            "participants",
            "platformId",
            "queueId",
            "gameCreation",
            "gameEndTimestamp",
            "gameDuration",
            "gameMode",
            "gameType",
            "gameVersion",
            "mapId",
            "puuid",
            "summonerName",
            "summonerId",
            "summonerLevel",
            "teamId",
            "win",
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
            "onMyWayPings",
            "enemyMissingPings",
            "enemyVisionPings",
            "lane",
            "individualPosition",
            "teamPosition",
            "champExperience",
            "champLevel",
            "championId",
            "championName",
            "kills",
            "assists",
            "deaths",
            "kda",
            "killParticipation",
            "firstBloodAssist",
            "firstBloodKill",
            "soloKills",
            "doubleKills",
            "tripleKills",
            "quadraKills",
            "pentaKills",
            "longestTimeSpentLiving",
            "totalTimeSpentDead",
            "totalTimeCCDealt",
            "totalMinionsKilled",
            "neutralMinionsKilled",
            "laneMinionsFirst10Minutes",
            "jungleCsBefore10Minutes",
            "maxLevelLeadLaneOpponent",
            "maxCsAdvantageOnLaneOpponent",
            "goldEarned",
            "goldSpent",
            "goldPerMinute",
            "goldDiffAt10",
            "goldDiffAt15",
            "expDiffAt10",
            "expDiffAt15",
            "csDiffAt10",
            "csDiffAt15",
            "abilityUses",
            "spell1Casts",
            "spell2Casts",
            "spell3Casts",
            "spell4Casts",
            "summoner1Casts",
            "summoner1Id",
            "summoner2Casts",
            "summoner2Id",
            "item0",
            "item1",
            "item2",
            "item3",
            "item4",
            "item5",
            "item6",
            "itemsPurchased",
            "timeCCingOthers",
            "enemyChampionImmobilizations",
            "damageDealtToBuildings",
            "damageDealtToObjectives",
            "damageDealtToTurrets",
            "damageSelfMitigated",
            "magicDamageDealt",
            "magicDamageDealtToChampions",
            "magicDamageTaken",
            "physicalDamageDealt",
            "physicalDamageDealtToChampions",
            "physicalDamageTaken",
            "totalDamageDealt",
            "totalDamageDealtToChampions",
            "totalDamageShieldedOnTeammates",
            "totalDamageTaken",
            "totalHeal",
            "totalHealsOnTeammates",
            "trueDamageDealt",
            "trueDamageDealtToChampions",
            "trueDamageTaken",
            "damagePerMinute",
            "teamDamagePercentage",
            "damageTakenOnTeamPercentage",
            "visionScore",
            "visionScorePerMinute",
            "wardsPlaced",
            "controlWardsPlaced",
            "stealthWardsPlaced",
            "wardTakedowns",
            "wardsKilled",
            "wardsGuarded",
            "dragonTakedowns",
            "baronTakedowns",
            "firstTowerAssist",
            "firstTowerKill",
            "turretKills",
            "turretTakedowns",
            "turretsLost",
            "inhibitorKills",
            "inhibitorTakedowns",
            "inhibitorsLost",
            "nexusKills",
            "nexusLost",
            "bans1TeamId100",
            "bans2TeamId100",
            "bans3TeamId100",
            "bans4TeamId100",
            "bans5TeamId100",
            "baronFirstTeamId100",
            "baronKillsTeamId100",
            "championFirstTeamId100",
            "championKillsTeamId100",
            "dragonFirstTeamId100",
            "dragonKillsTeamId100",
            "inhibitorFirstTeamId100",
            "inhibitorKillsTeamId100",
            "riftHeraldFirstTeamId100",
            "riftHeraldKillsTeamId100",
            "towerFirstTeamId100",
            "towerKillsTeamId100",
            "bans1TeamId200",
            "bans2TeamId200",
            "bans3TeamId200",
            "bans4TeamId200",
            "bans5TeamId200",
            "baronFirstTeamId200",
            "baronKillsTeamId200",
            "championFirstTeamId200",
            "championKillsTeamId200",
            "dragonFirstTeamId200",
            "dragonKillsTeamId200",
            "inhibitorFirstTeamId200",
            "inhibitorKillsTeamId200",
            "riftHeraldFirstTeamId200",
            "riftHeraldKillsTeamId200",
            "towerFirstTeamId200",
            "towerKillsTeamId200"
        ]
    )

    # Scrapping

    n = 1
    print(f"On va scrapper les {n*100} derniers matchs de {summoner_name} :")
    print()
    match_id_list = []
    for i in range (0,n*100,100):

        print(f"Etape numéro {(i//100+1)} sur {n}")

        match_list = lol_watcher.match.by_puuid(
            region="europe",
            encrypted_puuid=summoner_info["puuid"],
            queue_id=queue_id,
            start=i,
            count=100)
        
        
        # define dataframe schema for output
        lol_df_inter = pd.DataFrame(
            columns=[
                "matchId",
                "participants",
                "platformId",
                "queueId",
                "gameCreation",
                "gameEndTimestamp",
                "gameDuration",
                "gameMode",
                "gameType",
                "gameVersion",
                "mapId",
                "puuid",
                "summonerName",
                "summonerId",
                "summonerLevel",
                "teamId",
                "win",
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
                "onMyWayPings",
                "enemyMissingPings",
                "enemyVisionPings",
                "lane",
                "individualPosition",
                "teamPosition",
                "champExperience",
                "champLevel",
                "championId",
                "championName",
                "kills",
                "assists",
                "deaths",
                "kda",
                "killParticipation",
                "firstBloodAssist",
                "firstBloodKill",
                "soloKills",
                "doubleKills",
                "tripleKills",
                "quadraKills",
                "pentaKills",
                "longestTimeSpentLiving",
                "totalTimeSpentDead",
                "totalTimeCCDealt",
                "totalMinionsKilled",
                "neutralMinionsKilled",
                "laneMinionsFirst10Minutes",
                "jungleCsBefore10Minutes",
                "maxLevelLeadLaneOpponent",
                "maxCsAdvantageOnLaneOpponent",
                "goldEarned",
                "goldSpent",
                "goldPerMinute",
                "goldDiffAt10",
                "goldDiffAt15",
                "expDiffAt10",
                "expDiffAt15",
                "csDiffAt10",
                "csDiffAt15",
                "abilityUses",
                "spell1Casts",
                "spell2Casts",
                "spell3Casts",
                "spell4Casts",
                "summoner1Casts",
                "summoner1Id",
                "summoner2Casts",
                "summoner2Id",
                "item0",
                "item1",
                "item2",
                "item3",
                "item4",
                "item5",
                "item6",
                "itemsPurchased",
                "timeCCingOthers",
                "enemyChampionImmobilizations",
                "damageDealtToBuildings",
                "damageDealtToObjectives",
                "damageDealtToTurrets",
                "damageSelfMitigated",
                "magicDamageDealt",
                "magicDamageDealtToChampions",
                "magicDamageTaken",
                "physicalDamageDealt",
                "physicalDamageDealtToChampions",
                "physicalDamageTaken",
                "totalDamageDealt",
                "totalDamageDealtToChampions",
                "totalDamageShieldedOnTeammates",
                "totalDamageTaken",
                "totalHeal",
                "totalHealsOnTeammates",
                "trueDamageDealt",
                "trueDamageDealtToChampions",
                "trueDamageTaken",
                "damagePerMinute",
                "teamDamagePercentage",
                "damageTakenOnTeamPercentage",
                "visionScore",
                "visionScorePerMinute",
                "wardsPlaced",
                "controlWardsPlaced",
                "stealthWardsPlaced",
                "wardTakedowns",
                "wardsKilled",
                "wardsGuarded",
                "dragonTakedowns",
                "baronTakedowns",
                "firstTowerAssist",
                "firstTowerKill",
                "turretKills",
                "turretTakedowns",
                "turretsLost",
                "inhibitorKills",
                "inhibitorTakedowns",
                "inhibitorsLost",
                "nexusKills",
                "nexusLost",
                "bans1TeamId100",
                "bans2TeamId100",
                "bans3TeamId100",
                "bans4TeamId100",
                "bans5TeamId100",
                "baronFirstTeamId100",
                "baronKillsTeamId100",
                "championFirstTeamId100",
                "championKillsTeamId100",
                "dragonFirstTeamId100",
                "dragonKillsTeamId100",
                "inhibitorFirstTeamId100",
                "inhibitorKillsTeamId100",
                "riftHeraldFirstTeamId100",
                "riftHeraldKillsTeamId100",
                "towerFirstTeamId100",
                "towerKillsTeamId100",
                "bans1TeamId200",
                "bans2TeamId200",
                "bans3TeamId200",
                "bans4TeamId200",
                "bans5TeamId200",
                "baronFirstTeamId200",
                "baronKillsTeamId200",
                "championFirstTeamId200",
                "championKillsTeamId200",
                "dragonFirstTeamId200",
                "dragonKillsTeamId200",
                "inhibitorFirstTeamId200",
                "inhibitorKillsTeamId200",
                "riftHeraldFirstTeamId200",
                "riftHeraldKillsTeamId200",
                "towerFirstTeamId200",
                "towerKillsTeamId200"
            ]
        )
        j=0
        for match_id in match_list:
            time.sleep(2) # on peut essayer de diminuer le time.sleep à 1.2 = 120/100 (100 requetes en 2 minutes)
            print(f"match_id n°{j}: {match_id}")

            match_id_data = lol_watcher.match.by_match_id(
                region="europe",
                match_id=match_id
            )

            match_id_data_timeline = lol_watcher.match.timeline_by_match_id(
                region="europe",
                match_id=match_id
            )
            
            # retrieve the index of the participant player
            participant_index = match_id_data["metadata"]["participants"].index(summoner_info["puuid"])

            # except failures
            try:
                match_id_data["info"]["participants"][participant_index]["challenges"]["killParticipation"]
            except:
                killParticipation = None
            else:
                killParticipation = match_id_data["info"]["participants"][participant_index]["challenges"]["killParticipation"]
            
            try:
                match_id_data["info"]["participants"][participant_index]["challenges"]["maxLevelLeadLaneOpponent"]
            except:
                maxLevelLeadLaneOpponent = None
            else:
                maxLevelLeadLaneOpponent = match_id_data["info"]["participants"][participant_index]["challenges"]["maxLevelLeadLaneOpponent"]
            
            try:
                match_id_data["info"]["participants"][participant_index]["challenges"]["maxCsAdvantageOnLaneOpponent"]
            except:
                maxCsAdvantageOnLaneOpponent = None
            else:
                maxCsAdvantageOnLaneOpponent = match_id_data["info"]["participants"][participant_index]["challenges"]["maxCsAdvantageOnLaneOpponent"]
            
            try:
                match_id_data["info"]["participants"][participant_index]["challenges"]["teamDamagePercentage"]
            except:
                teamDamagePercentage = None
            else:
                teamDamagePercentage = match_id_data["info"]["participants"][participant_index]["challenges"]["teamDamagePercentage"]
            
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

            lol_df_inter = pd.concat(
                objs=[
                    lol_df_inter,
                    pd.DataFrame(
                        data=dict(
                            zip(
                                lol_df.columns,
                                [
                                    match_id_data["metadata"]["matchId"],
                                    ", ".join(match_id_data["metadata"]["participants"]),
                                    match_id_data["info"]["platformId"],
                                    match_id_data["info"]["queueId"],
                                    match_id_data["info"]["gameCreation"],
                                    match_id_data["info"]["gameEndTimestamp"],
                                    match_id_data["info"]["gameDuration"],
                                    match_id_data["info"]["gameMode"],
                                    match_id_data["info"]["gameType"],
                                    match_id_data["info"]["gameVersion"],
                                    match_id_data["info"]["mapId"],
                                    match_id_data["info"]["participants"][participant_index]["puuid"],
                                    match_id_data["info"]["participants"][participant_index]["summonerName"],
                                    match_id_data["info"]["participants"][participant_index]["summonerId"],
                                    match_id_data["info"]["participants"][participant_index]["summonerLevel"],
                                    match_id_data["info"]["participants"][participant_index]["teamId"],
                                    match_id_data["info"]["participants"][participant_index]["win"],
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
                                    match_id_data["info"]["participants"][participant_index].get("onMyWayPings", None),
                                    match_id_data["info"]["participants"][participant_index].get("enemyMissingPings", None),
                                    match_id_data["info"]["participants"][participant_index].get("enemyVisionPings", None),
                                    match_id_data["info"]["participants"][participant_index]["lane"],
                                    match_id_data["info"]["participants"][participant_index]["individualPosition"],
                                    match_id_data["info"]["participants"][participant_index]["teamPosition"],
                                    match_id_data["info"]["participants"][participant_index]["champExperience"],
                                    match_id_data["info"]["participants"][participant_index]["champLevel"],
                                    match_id_data["info"]["participants"][participant_index]["championId"],
                                    match_id_data["info"]["participants"][participant_index]["championName"],
                                    match_id_data["info"]["participants"][participant_index]["kills"],
                                    match_id_data["info"]["participants"][participant_index]["assists"],
                                    match_id_data["info"]["participants"][participant_index]["deaths"],
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["kda"],
                                    killParticipation,
                                    match_id_data["info"]["participants"][participant_index]["firstBloodAssist"],
                                    match_id_data["info"]["participants"][participant_index]["firstBloodKill"],
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["soloKills"],
                                    match_id_data["info"]["participants"][participant_index]["doubleKills"],
                                    match_id_data["info"]["participants"][participant_index]["tripleKills"],
                                    match_id_data["info"]["participants"][participant_index]["quadraKills"],
                                    match_id_data["info"]["participants"][participant_index]["pentaKills"],
                                    match_id_data["info"]["participants"][participant_index]["longestTimeSpentLiving"],
                                    match_id_data["info"]["participants"][participant_index]["totalTimeSpentDead"],
                                    match_id_data["info"]["participants"][participant_index]["totalTimeCCDealt"],
                                    match_id_data["info"]["participants"][participant_index]["totalMinionsKilled"],
                                    match_id_data["info"]["participants"][participant_index]["neutralMinionsKilled"],
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["laneMinionsFirst10Minutes"],
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["jungleCsBefore10Minutes"],
                                    maxLevelLeadLaneOpponent,
                                    maxCsAdvantageOnLaneOpponent,
                                    match_id_data["info"]["participants"][participant_index]["goldEarned"],
                                    match_id_data["info"]["participants"][participant_index]["goldSpent"],
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["goldPerMinute"],
                                    goldDiffAt10,
                                    goldDiffAt15,
                                    expDiffAt10,
                                    expDiffAt15,
                                    csDiffAt10,
                                    csDiffAt15,
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["abilityUses"],
                                    match_id_data["info"]["participants"][participant_index]["spell1Casts"],
                                    match_id_data["info"]["participants"][participant_index]["spell2Casts"],
                                    match_id_data["info"]["participants"][participant_index]["spell3Casts"],
                                    match_id_data["info"]["participants"][participant_index]["spell4Casts"],
                                    match_id_data["info"]["participants"][participant_index]["summoner1Casts"],
                                    match_id_data["info"]["participants"][participant_index]["summoner1Id"],
                                    match_id_data["info"]["participants"][participant_index]["summoner2Casts"],
                                    match_id_data["info"]["participants"][participant_index]["summoner2Id"],
                                    match_id_data["info"]["participants"][participant_index]["item0"],
                                    match_id_data["info"]["participants"][participant_index]["item1"],
                                    match_id_data["info"]["participants"][participant_index]["item2"],
                                    match_id_data["info"]["participants"][participant_index]["item3"],
                                    match_id_data["info"]["participants"][participant_index]["item4"],
                                    match_id_data["info"]["participants"][participant_index]["item5"],
                                    match_id_data["info"]["participants"][participant_index]["item6"],
                                    match_id_data["info"]["participants"][participant_index]["itemsPurchased"],
                                    match_id_data["info"]["participants"][participant_index]["timeCCingOthers"],
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["enemyChampionImmobilizations"],
                                    match_id_data["info"]["participants"][participant_index]["damageDealtToBuildings"],
                                    match_id_data["info"]["participants"][participant_index]["damageDealtToObjectives"],
                                    match_id_data["info"]["participants"][participant_index]["damageDealtToTurrets"],
                                    match_id_data["info"]["participants"][participant_index]["damageSelfMitigated"],
                                    match_id_data["info"]["participants"][participant_index]["magicDamageDealt"],
                                    match_id_data["info"]["participants"][participant_index]["magicDamageDealtToChampions"],
                                    match_id_data["info"]["participants"][participant_index]["magicDamageTaken"],
                                    match_id_data["info"]["participants"][participant_index]["physicalDamageDealt"],
                                    match_id_data["info"]["participants"][participant_index]["physicalDamageDealtToChampions"],
                                    match_id_data["info"]["participants"][participant_index]["physicalDamageTaken"],
                                    match_id_data["info"]["participants"][participant_index]["totalDamageDealt"],
                                    match_id_data["info"]["participants"][participant_index]["totalDamageDealtToChampions"],
                                    match_id_data["info"]["participants"][participant_index]["totalDamageShieldedOnTeammates"],
                                    match_id_data["info"]["participants"][participant_index]["totalDamageTaken"],
                                    match_id_data["info"]["participants"][participant_index]["totalHeal"],
                                    match_id_data["info"]["participants"][participant_index]["totalHealsOnTeammates"],
                                    match_id_data["info"]["participants"][participant_index]["trueDamageDealt"],
                                    match_id_data["info"]["participants"][participant_index]["trueDamageDealtToChampions"],
                                    match_id_data["info"]["participants"][participant_index]["trueDamageTaken"],
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["damagePerMinute"],
                                    teamDamagePercentage,
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["damageTakenOnTeamPercentage"],
                                    match_id_data["info"]["participants"][participant_index]["visionScore"],
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["visionScorePerMinute"],
                                    match_id_data["info"]["participants"][participant_index]["wardsPlaced"],
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["controlWardsPlaced"],
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["stealthWardsPlaced"],
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["wardTakedowns"],
                                    match_id_data["info"]["participants"][participant_index]["wardsKilled"],
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["wardsGuarded"],
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["dragonTakedowns"],
                                    match_id_data["info"]["participants"][participant_index]["challenges"]["baronTakedowns"],
                                    match_id_data["info"]["participants"][participant_index]["firstTowerAssist"],
                                    match_id_data["info"]["participants"][participant_index]["firstTowerKill"],
                                    match_id_data["info"]["participants"][participant_index]["turretKills"],
                                    match_id_data["info"]["participants"][participant_index]["turretTakedowns"],
                                    match_id_data["info"]["participants"][participant_index]["turretsLost"],
                                    match_id_data["info"]["participants"][participant_index]["inhibitorKills"],
                                    match_id_data["info"]["participants"][participant_index]["inhibitorTakedowns"],
                                    match_id_data["info"]["participants"][participant_index]["inhibitorsLost"],
                                    match_id_data["info"]["participants"][participant_index]["nexusKills"],
                                    match_id_data["info"]["participants"][participant_index]["nexusLost"],
                                    match_id_data["info"]["teams"][0]["bans"][0]["championId"],
                                    match_id_data["info"]["teams"][0]["bans"][1]["championId"],
                                    match_id_data["info"]["teams"][0]["bans"][2]["championId"],
                                    match_id_data["info"]["teams"][0]["bans"][3]["championId"],
                                    match_id_data["info"]["teams"][0]["bans"][4]["championId"],
                                    match_id_data["info"]["teams"][0]["objectives"]["baron"]["first"],
                                    match_id_data["info"]["teams"][0]["objectives"]["baron"]["kills"],
                                    match_id_data["info"]["teams"][0]["objectives"]["champion"]["first"],
                                    match_id_data["info"]["teams"][0]["objectives"]["champion"]["kills"],
                                    match_id_data["info"]["teams"][0]["objectives"]["dragon"]["first"],
                                    match_id_data["info"]["teams"][0]["objectives"]["dragon"]["kills"],
                                    match_id_data["info"]["teams"][0]["objectives"]["inhibitor"]["first"],
                                    match_id_data["info"]["teams"][0]["objectives"]["inhibitor"]["kills"],
                                    match_id_data["info"]["teams"][0]["objectives"]["riftHerald"]["first"],
                                    match_id_data["info"]["teams"][0]["objectives"]["riftHerald"]["kills"],
                                    match_id_data["info"]["teams"][0]["objectives"]["tower"]["first"],
                                    match_id_data["info"]["teams"][0]["objectives"]["tower"]["kills"],
                                    match_id_data["info"]["teams"][1]["bans"][0]["championId"],
                                    match_id_data["info"]["teams"][1]["bans"][1]["championId"],
                                    match_id_data["info"]["teams"][1]["bans"][2]["championId"],
                                    match_id_data["info"]["teams"][1]["bans"][3]["championId"],
                                    match_id_data["info"]["teams"][1]["bans"][4]["championId"],
                                    match_id_data["info"]["teams"][1]["objectives"]["baron"]["first"],
                                    match_id_data["info"]["teams"][1]["objectives"]["baron"]["kills"],
                                    match_id_data["info"]["teams"][1]["objectives"]["champion"]["first"],
                                    match_id_data["info"]["teams"][1]["objectives"]["champion"]["kills"],
                                    match_id_data["info"]["teams"][1]["objectives"]["dragon"]["first"],
                                    match_id_data["info"]["teams"][1]["objectives"]["dragon"]["kills"],
                                    match_id_data["info"]["teams"][1]["objectives"]["inhibitor"]["first"],
                                    match_id_data["info"]["teams"][1]["objectives"]["inhibitor"]["kills"],
                                    match_id_data["info"]["teams"][1]["objectives"]["riftHerald"]["first"],
                                    match_id_data["info"]["teams"][1]["objectives"]["riftHerald"]["kills"],
                                    match_id_data["info"]["teams"][1]["objectives"]["tower"]["first"],
                                    match_id_data["info"]["teams"][1]["objectives"]["tower"]["kills"]
                                ]
                            )
                        ),
                        index=[0]
                    )
                ],
                axis=0,
                join="outer",
                ignore_index=True
            )
            j+=1
        # Ajouter le contenu de lol_df au DataFrame initial
        lol_df = pd.concat([lol_df, lol_df_inter], ignore_index=True)

    print("Bravo it's done")
    print(lol_df.shape)

    # Sauvegarder le nouveau DataFrame dans le même fichier pickle
    with open(f'lol_df_{summoner_name}.pkl', 'wb') as f:
        pickle.dump(lol_df, f)
