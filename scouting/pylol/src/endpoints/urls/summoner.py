# -*- coding: utf-8 -*-

class SummonerUrl:
    """
    Class that returns, for each method, the API Summoner-v4 endpoint name to use
    to build URL and query parameters.
    """
    by_account_id = "/summoner/v4/summoners/by-account/{encryptedAccountId}"
    by_summoner_name = "/summoner/v4/summoners/by-name/{summonerName}"
    by_puuid = "/summoner/v4/summoners/by-puuid/{encryptedPUUID}"
    by_summoner_id = "/summoner/v4/summoners/{encryptedSummonerId}"