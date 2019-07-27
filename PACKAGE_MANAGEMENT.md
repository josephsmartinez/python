# Anaconda and Pythons Installations

## AWS Deployments

Packaging and zip for lambda (using conda)

> conda list --export > requirements.txt
> pip install -r requirements.txt -t .
> zip -r Archive.zip .

## Convert IPython to .py file

> jupyter nbconvert --to script [YOUR_NOTEBOOK].ipynb

## install from install script

> wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
> sh Anaconda3-2019.03-Linux-x86_64.sh

## Using anaconda (conda)

> conda list
> conda info --envs
> conda create --name myenv
> conda activate
> conda deactivate
> conda env create -f example.yml
> conda env export > /home/YOUR_NAME/Documents/example.yml

pip freeze, like conda list --export, is more for generating requirements files for your environment. For example, if you have created a package in your customized environment with certain dependencies, you can do conda list --export > requirements.txt. When you are ready to distribute your package to other users, they can easily duplicate your environment and the associated dependencies with conda create --name <envname> --file requirements.txt.
> conda list --export > requirements.txt
> conda create --name <envname> --file requirements.txt

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

Managing packages
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html

Anaconda Documentation
https://docs.anaconda.com/

Anaconda 2019.03 for Linux Installer
https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh

Installing Python 3.7 on CentOS 7
https://linuxacademy.com/devops/training/lesson/course/intro-to-python-development/name/installing-python-3-7-on-cent-os-7

IUS is a community project that provides RPM packages for newer versions of select software for Enterprise Linux distributions.
https://ius.io/
