from setuptools import setup, find_packages

version = "0.0.1"
description = "Python library for requesting League of Legends data from the Riot Game API."
long_description = "Python library that simplifies data querying on 5 League of Legends endpoints from the Riot Game API. This library provides easy access to champion mastery, league, challenges, match and summoner endpoints. The information returned by the API can then be used for all your projects."

setup(
        name="pylol", 
        version=version,
        author="pylol",
        author_email="n/a",
        description=description,
        long_description=long_description,
        packages=["pylol"],
        install_requires=["requests"],
        keywords=["python", "league-of-legends", "lol", "riot", "endpoints"],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: Free For Home Use",
            "Operating System :: MacOS",
            "Operating System :: Microsoft",
            "Operating System :: Unix",
            "Programming Language :: Python :: 3"
        ]
)