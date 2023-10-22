# -*- coding: utf-8 -*-

class ChallengesUrl:
    """
    Class that returns, for each method, the API Challenges-v1 endpoint name to use
    to build URL and query parameters.
    """
    percentiles = "/challenges/v1/challenges/percentiles"
    config_by_challenge_id = "/challenges/v1/challenges/{challengeId}/config"
    percentiles_by_challenge_id = "/challenges/v1/challenges/{challengeId}/percentiles"
    by_puuid = "/challenges/v1/player-data/{encryptedPUUID}"