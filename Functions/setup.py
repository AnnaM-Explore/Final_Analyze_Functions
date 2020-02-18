from setuptools import setup

setup(
    name='Functions',
    version='1.0',
    description='A useful set of functions for Eskom analytics team to calculate and analyse metrics.',
    author='Team 1',
    author_email='',
    packages=['Functions'],  #same as name
    install_requires=['pandas', 'numpy'], #external packages as dependencies
)