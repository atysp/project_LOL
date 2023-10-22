# -*- coding: utf-8 -*-

class LeagueUrl:
    """
    Class that returns, for each method, the API League-v4 endpoint name to use
    to build URL and query parameters.
    """
    challenger_by_queue = "/league/v4/challengerleagues/by-queue/{queue}"
    grandmaster_by_queue = "/league/v4/grandmasterleagues/by-queue/{queue}"
    master_by_queue = "/league/v4/masterleagues/by-queue/{queue}"
    by_league_id = "/league/v4/leagues/{leagueId}"
    by_summoner_id = "/league/v4/entries/by-summoner/{encryptedSummonerId}"