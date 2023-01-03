from setuptools import setup, find_packages

setup(
  name='ihsg-cli',
  packages=find_packages(),
  email='limkaleb@gmail.com',
  author='Lim Kaleb',
  install_requires=[
    'click',
    'yfinance',
    'colorama'
  ],
  version='0.0.0',
  entry_points='''
  [console_scripts]
  ihsg=ihsgcli:ihsgcli
  '''
)
