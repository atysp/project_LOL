# -*- coding: utf-8 -*-

import logging
import re
from typing import Literal

from api.config import BaseApi
from endpoints.urls.league import LeagueUrl

#define the log settings
logging.basicConfig(
    filename="src/api/api.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%y/%m/%d %H:%M:%S",
    level=logging.INFO
)


class LeagueEndpoint(BaseApi):
    """
    Class that wraps the League-v4 endpoint calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#league-v4 for more detailed information.

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

    def challenger_by_queue(
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
        queue: Literal[
            "ranked_solo_5x5",
            "ranked_flex_sr",
            "ranked_flex_tt"
        ]
        ) -> dict:
        """
        Get the Challenger league for a given queue.
        
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
        
        queue: str | Literal
            Filter players by a specific queue.
            Pick: {
                ranked_solo_5x5,
                ranked_flex_sr,
                ranked_flex_tt
            }

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'queue' parameter must be a string.

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
        
        if isinstance(queue, str):
            queue = queue.upper()
            queue = re.sub(
                pattern="X",
                repl="x",
                string=queue
            )
        else:
            raise TypeError(
                f"'queue' parameter must be a str: got {type(queue)}"
            )
        
        self.logger.info("League-v4: get the Challenger league for a given queue")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=LeagueUrl.challenger_by_queue.format(
                queue=queue
            )
        )

    def grandmaster_by_queue(
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
        queue: Literal[
            "ranked_solo_5x5",
            "ranked_flex_sr",
            "ranked_flex_tt"
        ]
        ) -> dict:
        """
        Get the GrandMaster league for a given queue.
        
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
        
        queue: str | Literal
            Filter players by a specific queue.
            Pick: {
                ranked_solo_5x5,
                ranked_flex_sr,
                ranked_flex_tt
            }

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'queue' parameter must be a string.

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
        
        if isinstance(queue, str):
            queue = queue.upper()
            queue = re.sub(
                pattern="X",
                repl="x",
                string=queue
            )
        else:
            raise TypeError(
                f"'queue' parameter must be a str: got {type(queue)}"
            )
        
        self.logger.info("League-v4: get the GrandMaster league for a given queue")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=LeagueUrl.grandmaster_by_queue.format(
                queue=queue
            )
        )

    def master_by_queue(
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
        queue: Literal[
            "ranked_solo_5x5",
            "ranked_flex_sr",
            "ranked_flex_tt"
        ]
        ) -> dict:
        """
        Get the Master league for a given queue.
        
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
        
        queue: str | Literal
            Filter players by a specific queue.
            Pick: {
                ranked_solo_5x5,
                ranked_flex_sr,
                ranked_flex_tt
            }

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'queue' parameter must be a string.

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
        
        if isinstance(queue, str):
            queue = queue.upper()
            queue = re.sub(
                pattern="X",
                repl="x",
                string=queue
            )
        else:
            raise TypeError(
                f"'queue' parameter must be a str: got {type(queue)}"
            )
        
        self.logger.info("League-v4: get the Master league for a given queue")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=LeagueUrl.master_by_queue.format(
                queue=queue
            )
        )

    def by_league_id(
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
        league_id: str
        ) -> dict:
        """
        Get league with given ID, including inactive entries.
        
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
        
        league_id: str
            League ID to query.

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'league_id' parameter must be a string.

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
        
        if isinstance(league_id, str):
            pass
        else:
            raise TypeError(
                f"'league_id' parameter must be a str: got {type(league_id)}"
            )
        
        self.logger.info("League-v4: get league entries by league id")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=LeagueUrl.by_league_id.format(
                leagueId=league_id
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
        ) -> list:
        """
        Get league entries in all queues for a given summoner ID.
        
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
        
        self.logger.info("League-v4: get league entries by summoner id")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=LeagueUrl.by_summoner_id.format(
                encryptedSummonerId=encrypted_summoner_id
            )
        )