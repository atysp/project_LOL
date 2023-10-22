# -*- coding: utf-8 -*-

import logging
from typing import Literal

from api.config import BaseApi
from endpoints.urls.champion import ChampionMasteryUrl

#define the log settings
logging.basicConfig(
    filename="src/api/api.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%y/%m/%d %H:%M:%S",
    level=logging.INFO
)


class ChampionMasteryEndpoint(BaseApi):
    """
    Class that wraps the Champion-Mastery-v4 endpoint calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#champion-mastery-v4 for more detailed information.

    Parameters
    ----------
    BaseApi: Python class
        BaseApi instance allows to send a get request by injecting the provided endpoint name
        into the method call.
    """
    def __init__(self, api_key: str) -> None:
        """
        Function that allows to build the BaseApi class and initialise all the
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
        
        super().__init__(api_key)

    def by_summoner_id(
        self,
        region: Literal[
            "br1",
            "eun1",
            "euw1",
            "la1",
            "la2",
            "na1",
            "oc1",
            "ru1",
            "tr1",
            "jp1",
            "kr",
            "ph2",
            "sg2",
            "tw2",
            "th2",
            "vn2"
        ],
        encrypted_summoner_id: str
        ) -> list:
        """
        Get all champion mastery entries by summoner ID (sorted by number of champion points descending).
        
        Parameters
        ----------
        region: str | Literal
            Region of the server to be queried.
            Pick local region: {
                Brazil: 'br1',
                Europe Nordic & East: 'eun1',
                Europe West: 'euw1',
                Latin America North: 'la1',
                Latin America South: 'la2',
                North America: 'na1',
                Oceania: 'oc1',
                Russia: 'ru1',
                Turkey: 'tr1',
                Japan: 'jp1',
                South Korea: 'kr',
                Philippines: 'ph2',
                Singapore, Malaysia, & Indonesia: 'sg2',
                Taiwan, Hong Kong, and Macao: 'tw2',
                Thailand: 'th2',
                Vietnam: 'vn2',
                Public Beta Environment: 'pbe'
            }

        encrypted_summoner_id: str
            Player's encrypted summoner ID.

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'encrypted_summoner_id' parameter must be a string.

        Returns
        -------
        list
            API response in json format.
        """
        #check the parameters consistency
        if isinstance(region, str):
            pass
        else:
            raise TypeError(
                f"'region' parameter must be a str: got {type(region)}"
            )
        
        if isinstance(encrypted_summoner_id, str):
            pass
        else:
            raise TypeError(
                f"'encrypted_summoner_id' parameter must be a str: got {type(encrypted_summoner_id)}"
            )
        
        self.logger.info("Champion-Mastery-v4: get champion mastery entries by summoner id")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=ChampionMasteryUrl.by_summoner_id.format(
                encryptedSummonerId=encrypted_summoner_id
            )
        )

    def by_summoner_champion_id(
        self,
        region: Literal[
            "br1",
            "eun1",
            "euw1",
            "la1",
            "la2",
            "na1",
            "oc1",
            "ru1",
            "tr1",
            "jp1",
            "kr",
            "ph2",
            "sg2",
            "tw2",
            "th2",
            "vn2"
        ],
        encrypted_summoner_id: str,
        champion_id: int
        ) -> dict:
        """
        Get a champion mastery by summoner ID and champion ID.
        
        Parameters
        ----------
        region: str | Literal
            Region of the server to be queried.
            Pick local region: {
                Brazil: 'br1',
                Europe Nordic & East: 'eun1',
                Europe West: 'euw1',
                Latin America North: 'la1',
                Latin America South: 'la2',
                North America: 'na1',
                Oceania: 'oc1',
                Russia: 'ru1',
                Turkey: 'tr1',
                Japan: 'jp1',
                South Korea: 'kr',
                Philippines: 'ph2',
                Singapore, Malaysia, & Indonesia: 'sg2',
                Taiwan, Hong Kong, and Macao: 'tw2',
                Thailand: 'th2',
                Vietnam: 'vn2',
                Public Beta Environment: 'pbe'
            }

        encrypted_summoner_id: str
            Player's encrypted summoner ID.

        champion_id: int
            Champion ID.

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'encrypted_summoner_id' parameter must be a string.
            - To use this function, the 'champion_id' parameter must be an integer.

        Returns
        -------
        int
            API response in json format.
        """
        #check the parameters consistency
        if isinstance(region, str):
            pass
        else:
            raise TypeError(
                f"'region' parameter must be a str: got {type(region)}"
            )
        
        if isinstance(encrypted_summoner_id, str):
            pass
        else:
            raise TypeError(
                f"'encrypted_summoner_id' parameter must be a str: got {type(encrypted_summoner_id)}"
            )
        
        if isinstance(champion_id, int):
            pass
        else:
            raise TypeError(
                f"'champion_id' parameter must be an int: got {type(champion_id)}"
            )
        
        self.logger.info("Champion-Mastery-v4: get champion mastery entries by summoner and champion id")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=ChampionMasteryUrl.by_summoner_champion_id.format(
                encryptedSummonerId=encrypted_summoner_id,
                championId=champion_id
            )
        )

    def score_by_summoner_id(
        self,
        region: Literal[
            "br1",
            "eun1",
            "euw1",
            "la1",
            "la2",
            "na1",
            "oc1",
            "ru1",
            "tr1",
            "jp1",
            "kr",
            "ph2",
            "sg2",
            "tw2",
            "th2",
            "vn2"
        ],
        encrypted_summoner_id: str
        ) -> int:
        """
        Get a player's total champion mastery score by summoner ID.
        
        Parameters
        ----------
        region: str | Literal
            Region of the server to be queried.
            Pick local region: {
                Brazil: 'br1',
                Europe Nordic & East: 'eun1',
                Europe West: 'euw1',
                Latin America North: 'la1',
                Latin America South: 'la2',
                North America: 'na1',
                Oceania: 'oc1',
                Russia: 'ru1',
                Turkey: 'tr1',
                Japan: 'jp1',
                South Korea: 'kr',
                Philippines: 'ph2',
                Singapore, Malaysia, & Indonesia: 'sg2',
                Taiwan, Hong Kong, and Macao: 'tw2',
                Thailand: 'th2',
                Vietnam: 'vn2',
                Public Beta Environment: 'pbe'
            }

        encrypted_summoner_id: str
            Player's encrypted summoner ID.

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'encrypted_summoner_id' parameter must be a string.

        Returns
        -------
        dict
            API response in json format.
        """
        #check the parameters consistency
        if isinstance(region, str):
            pass
        else:
            raise TypeError(
                f"'region' parameter must be a str: got {type(region)}"
            )
        
        if isinstance(encrypted_summoner_id, str):
            pass
        else:
            raise TypeError(
                f"'encrypted_summoner_id' parameter must be a str: got {type(encrypted_summoner_id)}"
            )
        
        self.logger.info("Champion-Mastery-v4: get total champion mastery score by summoner id")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=ChampionMasteryUrl.score_by_summoner_id.format(
                encryptedSummonerId=encrypted_summoner_id
            )
        )