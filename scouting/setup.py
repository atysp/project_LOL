from setuptools import setup, find_packages

setup(
    name="scouting",
    version="1.0",
    packages=["scouting" ,"scouting.pylol"],
    install_requires=[
        "numpy", "pandas", "requests", "bs4", "plotly", "scipy", "logging", "requests", "time", "typing"
    ],
)
