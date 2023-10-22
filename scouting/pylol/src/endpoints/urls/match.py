# -*- coding: utf-8 -*-

class MatchUrl:
    """
    Class that returns, for each method, the API Match-v5 endpoint name to use
    to build URL and query parameters.
    """
    by_puuid = "/match/v5/matches/by-puuid/{encryptedPUUID}/ids"
    by_match_id = "/match/v5/matches/{matchId}"
    timeline_by_match_id = "/match/v5/matches/{matchId}/timeline"