from setuptools import setup, find_packages

setup(
    name="scouting",
    version="1.0",
    packages=["scouting"],
    install_requires=[
        "numpy", "pandas", "requests", "bs4", "plotly", "scipy", "pylol"
    ],
)
