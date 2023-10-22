# -*- coding: utf-8 -*-

import logging

from endpoints import (
    champion,
    league,
    challenges,
    match,
    summoner
)

#define the log settings
logging.basicConfig(
    filename="src/api/api.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%y/%m/%d %H:%M:%S",
    level=logging.INFO
)


class LolWatcher:
    """
    Class intended to be the main point of interaction with the endpoints
    of the Riot Developer API for League of Legends.
    """
    def __init__(self, api_key: str) -> None:
        """
        Function that allows to build the LolWatcher class and initialise all the
        parameters necessary to the calls of the API.

        Parameters
        ----------
        api_key: str
            Personal development API key.

        Raises
        ------
        TypeError
            - To use this class, the 'api_key' parameter must be a string.

        Returns
        -------
        None
            NoneType.
        """
        #initialize the logs settings
        self.logger = logging.getLogger("Riot LoL API")
        
        #initialize the endpoints settings
        self._league = league.LeagueEndpoint(api_key=api_key)
        self._challenges = challenges.ChallengesEndpoint(api_key=api_key)
        self._match = match.MatchEndpoint(api_key=api_key)
        self._summoner = summoner.SummonerEndpoint(api_key=api_key)
    
    @property
    def champion_mastery(self) -> champion.ChampionMasteryEndpoint:
        """
        Interface to the Champion-Mastery-v4 endpoint.

        Returns
        -------
            champion.ChampionMasteryEndpoint: class
                Class that wraps the Champion-Mastery-v4 endpoint calls provided by the Riot API.
        """
        self.logger.warning("Connected to Champion-Mastery-v4 endpoint")
        return self._champion_mastery
    
    @property
    def league(self) -> league.LeagueEndpoint:
        """
        Interface to the League-v4 endpoint.

        Returns
        -------
            league.LeagueEndpoint: class
                Class that wraps the League-v4 endpoint calls provided by the Riot API.
        """
        self.logger.warning("Connected to League-v4 endpoint")
        return self._league
    
    @property
    def challenges(self) -> challenges.ChallengesEndpoint:
        """
        Interface to the Challenges-v1 endpoint.

        Returns
        -------
            challenges.ChallengesEndpoint: class
                Class that wraps the Challenges-v1 endpoint calls provided by the Riot API.
        """
        self.logger.warning("Connected to Challenges-v1 endpoint")
        return self._challenges
    
    @property
    def match(self) -> match.MatchEndpoint:
        """
        Interface to the Match-v5 endpoint.

        Returns
        -------
            match.MatchEndpoint: class
                Class that wraps the Match-v5 endpoint calls provided by the Riot API.
        """
        self.logger.warning("Connected to Match-v5 endpoint")
        return self._match
    
    @property
    def summoner(self) -> summoner.SummonerEndpoint:
        """
        Interface to the Summoner-v4 endpoint.

        Returns
        -------
            summoner.SummonerEndpoint: class
                Class that wraps the Summoner-v4 endpoint calls provided by the Riot API.
        """
        self.logger.warning("Connected to Summoner-v4 endpoint")
        return self._summoner