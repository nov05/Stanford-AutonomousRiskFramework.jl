from setuptools import setup, find_packages

setup(name='adv_carla',
      version='0.0.1',
      packages=find_packages(include=['adv_carla', 'adv_carla.*']),   ## added by nov05
      install_requires=['gym']) # TODO: other reqs.
