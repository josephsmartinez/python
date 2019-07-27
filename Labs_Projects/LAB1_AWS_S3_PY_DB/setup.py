from setuptools import find_packages, setup

with open('README.md', 'r') as f:
  long_decription= f.read()

setup(
  name='pgbackup',
  version='0.1.0',
  author='Mike Sneed',
  author_email='mikes@gmail.com',
  description='A utility for backing up PostgresSQL database',
  long_decription=long_decription,
  long_decription_content_type='text/markdown',
  url='https://github.com/linuxacademy/pgbackup',
  packages=find_packages('src')
)