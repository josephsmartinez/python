# Anaconda and Pythons Installations

## Convert IPython to .py file

> jupyter nbconvert --to script [YOUR_NOTEBOOK].ipynb

## install from install script

> wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
> sh Anaconda3-2019.03-Linux-x86_64.sh

## Using anaconda (conda)

> conda info --envs
> conda create --name myenv
> conda activate
> conda deactivate
> conda env create -f example.yml
> conda env export > /home/YOUR_NAME/Documents/example.yml

## pip

> pip3.7 install boto3
> pip3.7 freeze
> pip3.7 freeze > requirements.txt
> mkdir ~/venvs
> python3.7 -m venv ~/venvs/pg
> source ~/venvs/pg/bin/activate
> deactivate

## pipenv

> pip3.7 install --user pipenv
> mkdir ~/database
> cd ~/database
> pipenv --python python3.7

Resources:

Anaconda Documentation
https://docs.anaconda.com/

Anaconda 2019.03 for Linux Installer
https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh

Installing Python 3.7 on CentOS 7
https://linuxacademy.com/devops/training/lesson/course/intro-to-python-development/name/installing-python-3-7-on-cent-os-7

IUS is a community project that provides RPM packages for newer versions of select software for Enterprise Linux distributions.
https://ius.io/
