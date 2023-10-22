# -*- coding: utf-8 -*-

class ChampionMasteryUrl:
    """
    Class that returns, for each method, the API Champion Mastery-v4 endpoint name
    to use to build URL and query parameters.
    """
    by_summoner_id = "/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}"
    by_summoner_champion_id = "/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}/by-champion/{championId}"
    score_by_summoner_id = "/champion-mastery/v4/scores/by-summoner/{encryptedSummonerId}"