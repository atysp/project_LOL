# -*- coding: utf-8 -*-

import logging
from typing import Literal

from api.config import BaseApi
from endpoints.urls.challenges import ChallengesUrl

#define the log settings
logging.basicConfig(
    filename="src/api/api.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%y/%m/%d %H:%M:%S",
    level=logging.INFO
)


class ChallengesEndpoint(BaseApi):
    """
    Class that wraps the Challenges-v1 endpoint calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#challenges-v1 for more detailed information.

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

    def percentiles(
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
        ]
        ) -> dict:
        """
        Map of level to percentile of players who have achieved the challenges.

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

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.

        Returns
        -------
        dict
            API response in json format.
        """
        #check the parameter consistency
        if isinstance(region, str):
            pass
        else:
            raise TypeError(
                f"'region' parameter must be a str: got {type(region)}"
            )
        
        self.logger.info("Challenges-v1: get level to percentile of players who have achieved the challenges")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=ChallengesUrl.percentiles
        )

    def config_by_challenge_id(
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
        challenge_id: int
        ) -> dict:
        """
        Get challenge configuration by challenge ID.
        
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

        challenge_id: int
            Challenge ID.

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'challenge_id' parameter must be an integer.

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
        
        if isinstance(challenge_id, int):
            pass
        else:
            raise TypeError(
                f"'challenge_id' parameter must be an int: got {type(challenge_id)}"
            )
        
        self.logger.info("Challenges-v1: get challenge configuration by challenge id")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=ChallengesUrl.config_by_challenge_id.format(
                challengeId=challenge_id
            )
        )

    def percentiles_by_challenge_id(
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
        challenge_id: int
        ) -> dict:
        """
        Map of level to percentile of players who have achieved the challenge by challenge ID.
        
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

        challenge_id: int
            Challenge ID.

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'challenge_id' parameter must be an integer.

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
        
        if isinstance(challenge_id, int):
            pass
        else:
            raise TypeError(
                f"'challenge_id' parameter must be an int: got {type(challenge_id)}"
            )
        
        self.logger.info("Challenges-v1: get level to percentile of players who have achieved the challenge by challenge id")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=ChallengesUrl.percentiles_by_challenge_id.format(
                challengeId=challenge_id
            )
        )

    def by_puuid(
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
        encrypted_puuid: str
        ) -> dict:
        """
        Get player information with list of all progressed challenges by PUUID.
        
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

        encrypted_puuid: str
            Player's encrypted PUUID.

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'encrypted_puuid' parameter must be a string.

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
        
        if isinstance(encrypted_puuid, str):
            pass
        else:
            raise TypeError(
                f"'encrypted_puuid' parameter must be a str: got {type(encrypted_puuid)}"
            )
        
        self.logger.info("Challenges-v1: get challenge by PUUID")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=ChallengesUrl.by_puuid.format(
                encryptedPUUID=encrypted_puuid
            )
        )