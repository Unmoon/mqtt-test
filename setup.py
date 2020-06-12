from setuptools import find_packages
from setuptools import setup

setup(
    name="mqtt-test",
    version="0.0.1",
    url="https://github.com/Unmoon/mqtt-test",
    author="Unmoon",
    author_email="joona@unmoon.com",
    description="Simple example of multiple clients sending and receiving messages asynchronously.",
    packages=find_packages(),
    install_requires=[],
)
