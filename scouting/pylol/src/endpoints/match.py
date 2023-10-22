# -*- coding: utf-8 -*-

import logging
from typing import Literal

from api.config import BaseApi
from endpoints.urls.match import MatchUrl

#define the log settings
logging.basicConfig(
    filename="src/api/api.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%y/%m/%d %H:%M:%S",
    level=logging.INFO
)


class MatchEndpoint(BaseApi):
    """
    Class that wraps the Match-v5 endpoint calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#match-v5 for more detailed information.

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

    def by_puuid(
        self,
        region: Literal[
            "americas",
            "europe",
            "asia",
            "sea"
        ],
        encrypted_puuid: str,
        queue_id: int | None = None,
        start: int = 0,
        count: int = 20,
        start_time: int | None = None,
        end_time: int | None = None
        ) -> list:
        """
        Get a list of match ids by puuid.
        
        Parameters
        ----------
        region: str | Literal
            Region of the server to be queried.
            Pick global platform: {
                Americas: 'americas',
                Europe: 'europe',
                Asia: 'asia',
                South-East Asia: 'sea'
            }

        encrypted_puuid: str
            Player's encrypted PUUID.

        queue_id: int, optional, default=None
            Filter the match by a specific queue id.
            Pick: {
                Custom games: 0,
                All Random games: 325,
                5v5 ARAM games: 100, 450,
                5v5 Draft Pick games: 400,
                5v5 Blind Pick games: 430,
                5v5 Ranked Dynamic games: 410,
                5v5 Ranked Solo games: 420,
                5v5 Ranked Flex games: 440
            }
            Default is None.

        start: int, optional, default=None
            Start index of match.
            Default is 0.

        count: int, optional, default=None
            Number of match to return.
            Default is 20.

        start_time: int, optional, default=None
            Epoch timestamp filter in seconds. Match started storing
            timestamps on June 16th, 2021.
            Default is None.

        end_time: int, optional, default=None
            Epoch timestamp filter in seconds.
            Default is None.

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'encrypted_puuid' parameter must be a string.
            - To use this function, the 'queue_id' parameter must be an integer.
            - To use this function, the 'start' parameter must be an integer.
            - To use this function, the 'count' parameter must be an integer.
            - To use this function, the 'start_time' parameter must be an integer.
            - To use this function, the 'end_time' parameter must be an integer.

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
        
        if isinstance(encrypted_puuid, str):
            pass
        else:
            raise TypeError(
                f"'encrypted_puuid' parameter must be a str: got {type(encrypted_puuid)}"
            )
        
        if isinstance(queue_id, int):
            pass
        elif queue_id == None:
            pass
        else:
            raise TypeError(
                f"'queue_id' parameter must be an int: got {type(queue_id)}"
            )
        
        if isinstance(start, int):
            pass
        elif start == None:
            pass
        else:
            raise TypeError(
                f"'start' parameter must be an int: got {type(start)}"
            )
        
        if isinstance(count, int):
            pass
        elif count == None:
            pass
        else:
            raise TypeError(
                f"'count' parameter must be an int: got {type(count)}"
            )
        
        if isinstance(start_time, int):
            pass
        elif start_time == None:
            pass
        else:
            raise TypeError(
                f"'start_time' parameter must be an int: got {type(start_time)}"
            )
        
        if isinstance(end_time, int):
            pass
        elif end_time == None:
            pass
        else:
            raise TypeError(
                f"'end_time' parameter must be an int: got {type(end_time)}"
            )
        
        self.logger.info("Match-v5: get a list of match ids by puuid")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=MatchUrl.by_puuid.format(
                encryptedPUUID=encrypted_puuid,
            ),
            queue=queue_id,
            start=start,
            count=count,
            startTime=start_time,
            endTime=end_time
        )

    def by_match_id(
        self,
        region: Literal[
            "americas",
            "europe",
            "asia",
            "sea"
        ],
        match_id: str
        ) -> dict:
        """
        Get a match by match id.
        
        Parameters
        ----------
        region: str | Literal
            Region of the server to be queried.
            Pick global platform: {
                Americas: 'americas',
                Europe: 'europe',
                Asia: 'asia',
                South-East Asia: 'sea'
            }

        match_id: str
            Player's match ID.

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'match_id' parameter must be a string.

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
        
        if isinstance(match_id, str):
            pass
        else:
            raise TypeError(
                f"'match_id' parameter must be a str: got {type(match_id)}"
            )
        
        self.logger.info("Match-v5: get a match by match id")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=MatchUrl.by_match_id.format(
                matchId=match_id
            )
        )

    def timeline_by_match_id(
        self,
        region: Literal[
            "americas",
            "europe",
            "asia",
            "sea"
        ],
        match_id: str
        ) -> dict:
        """
        Get a match timeline by match id.
        
        Parameters
        ----------
        region: str | Literal
            Region of the server to be queried.
            Pick global platform: {
                Americas: 'americas',
                Europe: 'europe',
                Asia: 'asia',
                South-East Asia: 'sea'
            }

        match_id: str
            Player's match ID.

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'match_id' parameter must be a string.

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
        
        if isinstance(match_id, str):
            pass
        else:
            raise TypeError(
                f"'match_id' parameter must be a str: got {type(match_id)}"
            )
        
        self.logger.info("Match-v5: get a match timeline by match id")
        
        return self._request_endpoint(
            region=region,
            endpoint_name=MatchUrl.timeline_by_match_id.format(
                matchId=match_id
            )
        )
