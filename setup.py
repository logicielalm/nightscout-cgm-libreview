from setuptools import setup, find_packages

setup(
    name="nightscout-cgm-libreview",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        # other dependencies...
    ],
)