from setuptools import setup, find_packages

setup(
  name='ihsg-cli',
  version='0.0.1',
  packages=find_packages(),
  install_requires=[
    'click',
    'yfinance',
    'colorama'
  ],
  entry_points='''
  [console_scripts]
  ihsg=ihsgcli:ihsgcli
  '''
)
