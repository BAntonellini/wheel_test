# This is what your ‘setup.py’ file should look like.

from setuptools import find_packages, setup

setup(
    name="calc",  # Name
    version="1.0",  # Version
    packages=find_packages(),  # Automatically find the packages that are recognized in the '__init__.py'.
)
