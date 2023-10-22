# -*- coding: utf-8 -*-

import logging
import requests
import time

#define the log settings
logging.basicConfig(
    filename="src/api/api.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%y/%m/%d %H:%M:%S",
    level=logging.INFO
)


class BaseApi:
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
        #check the parameter consistency
        if isinstance(api_key, str):
            self.api_key = api_key
        else:
            raise TypeError(
                f"'api_key' parameter must be a str: got {type(api_key)}"
            )
        
        #initialize the session object
        self.session = requests.Session()
    
    def _request_endpoint(self, region: str, endpoint_name: str, **kwargs):
        """
        Function that sends a get request through the BaseApi instance provided,
        by injecting the provided endpoint name into the method call.

        Parameters
        ----------
        region: str
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
            Pick global platform: {
                Americas: 'americas',
                Europe: 'europe',
                Asia: 'asia',
                South-East Asia: 'sea'
            }

        endpoint_name: str
            The endpoint name to use to build URL and query parameters.

        Raises
        ------
        TypeError
            - To use this function, the 'region' parameter must be a string.
            - To use this function, the 'endpoint_name' parameter must be a string.

        ValueError
            - To have an answer to the get request, the status code must not be in error.

        Returns
        -------
        dict or list
            API response in json format.
        """
        #check the parameters consistency
        if isinstance(region, str):
            region = region.lower()
        else:
            raise TypeError(
                f"'region' parameter must be a str: got {type(region)}"
            )
        
        if isinstance(endpoint_name, str):
            pass
        else:
            raise TypeError(
                f"'endpoint_name' parameter must be a str: got {type(endpoint_name)}"
            )
        
        #initialize the logs settings
        logger = logging.getLogger("API settings")
        logger.warning("Connected to API settings")
        
        #define the league of legends API endpoint
        url = f"https://{region}.api.riotgames.com/lol{endpoint_name}"
        
        #get url request by managing the exceptions
        response = self.session.get(
            url=url,
            params={
                "api_key": self.api_key,
                **kwargs
            }
        )
        
        if response.status_code == 200:
            logger.info(
                f"API status code {response.status_code}: query completed"
            )
        elif response.status_code == 429:
            logger.error(
                f"API status code {response.status_code}: {response.json()['status']['message']}"
            )
        elif response.status_code in [400, 401, 403, 404, 405, 415, 500, 502, 503, 504]:
            logger.error(
                f"API status code {response.status_code}: {response.json()['status']['message']}"
            )
            raise ValueError(
                f"API status code: {response.status_code}, {response.json()['status']['message']}"
            )
        
        return response.json()