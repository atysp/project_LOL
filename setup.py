from setuptools import setup, find_packages

setup(
    name="project_LOL",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "numpy", "pandas", "requests", "bs4", "plotly", "scipy", "logging", "requests", "time", "typing"
    ],
)