
from setuptools import setup, find_packages

setup(
    name="kipi",
    version="0.1.0",
    description="http server to let others reset minecraft server remotely",
    author="Dean Lawrence",
    author_email="djlawren@umich.edu",
    packages=find_packages(),
    install_requires=[
        "flask",
        "gunicorn"
    ],
    entry_points=[]
)
