from setuptools import setup, find_packages

setup(
  name='ihsgstockinfo',
  packages=find_packages(),
  email='limkaleb@gmail.com',
  author='Lim Kaleb',
  install_requires=[
    'click',
    'yfinance',
    'colorama'
  ],
  version='0.0.0',
  description='''The description of the package''',
  entry_points='''
  [console_scripts]
  ihsgstockinfo=ihsgstockinfo:ihsgstockinfo
  '''
)
