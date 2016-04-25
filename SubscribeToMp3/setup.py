from setuptools import setup
setup(
  name = 'SubscribeToMp3',
  packages = ['SubscribeToMp3'], # this must be the same as the name above
  version = '0.1',
  description = 'Download songs from artists on soundcloud',
  author = 'Gilad y',
  url = 'https://github.com/peterldowns/mypackage', # use the URL to the github repo
  keywords = ['soundcloud', 'logging', 'example'], # arbitrary keywords
  install_requires=['soundcloud'],
)