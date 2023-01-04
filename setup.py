from setuptools import setup, find_packages

setup(
  name='ihsginfo-cli',
  packages=find_packages(),
  email='limkaleb@gmail.com',
  author='Lim Kaleb',
  install_requires=[
    'click',
    'yfinance',
    'colorama'
  ],
  version='0.0.2',
  description='''The description of the package''',
  entry_points='''
  [console_scripts]
  ihsginfo=ihsginfocli:cli
  '''
)
