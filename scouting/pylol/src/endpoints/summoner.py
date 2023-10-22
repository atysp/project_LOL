# -*- coding: utf-8 -*-

import logging
from typing import Literal

from api.config import BaseApi
from endpoints.urls.summoner import SummonerUrl


#define the log settings
logging.basicConfig(
    filename="src/api/api.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%y/%m/%d %H:%M:%S",
    level=logging.INFO
)


class SummonerEndpoint(BaseApi):
    """
    Class that wraps the Summoner-v4 endpoint calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#summoner-v4 for more detailed information.

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

    def by_account_id(
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
        encrypted_account_id: str
        ) -> dict:
        """
        Get a summoner by account ID.

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

        encrypted_account_id: str
            Player's encrypted account ID.

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'encrypted_account_id' parameter must be a string.

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
        
        if isinstance(encrypted_account_id, str):
            pass
        else:
            raise TypeError(
                f"'encrypted_account_id' parameter must be a str: got {type(encrypted_account_id)}"
            )
        
        self.logger.info("Summoner-v4: get summoner by account id")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=SummonerUrl.by_account_id.format(
                encryptedAccountId=encrypted_account_id
            )
        )

    def by_summoner_name(
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
        summoner_name: str
        ) -> dict:
        """
        Get a summoner by summoner name.

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

        summoner_name: str
            Player's summoner name.

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'summoner_name' parameter must be a string.

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
        
        if isinstance(summoner_name, str):
            pass
        else:
            raise TypeError(
                f"'summoner_name' parameter must be a str: got {type(summoner_name)}"
            )
        
        self.logger.info("Summoner-v4: get summoner by summoner name")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=SummonerUrl.by_summoner_name.format(
                summonerName=summoner_name
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
        Get a summoner by PUUID.
        
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
        
        self.logger.info("Summoner-v4: get summoner by PUUID")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=SummonerUrl.by_puuid.format(
                encryptedPUUID=encrypted_puuid
            )
        )

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
        ) -> dict:
        """
        Get a summoner by summoner ID.
        
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
        
        self.logger.info("Summoner-v4: get summoner by summoner id")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=SummonerUrl.by_summoner_id.format(
                encryptedSummonerId=encrypted_summoner_id
            )
        )