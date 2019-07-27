# Building a CLI Utility with Python, EC2, Docker, S3

## Setting up PostgreSQL Cloud Playground

Before we begin, we're going to need to need a PostgreSQL database to work with. The code repository for this course contains a db_setup.sh script that we'll use on a CentOS 7 Cloud Playground to create and run our database. Create a "CentOS 7" Cloud Playground and run the following on it:
> curl -o db_setup.sh https://raw.githubusercontent.com/linuxacademy/content-python-for-sys-admins/master/helpers/db_setup.sh

## Installing The Postgres 9.6 Client

On our development machines, we'll need to make sure that we have the Postgres client installed. The version needs to be 9.6.

On Red-hat systems we'll use the following:

> wget https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm
> sudo yum install pgdg-centos96-9.6-3.noarch.rpm epel-release
> sudo yum update
> sudo yum install postgresql96

On debian systems, the equivalent would be:
> sudo apt-get install postgres-client-9.6
or
>  sudo apt-get install postgresql-client

## Test connection from Workstation

Let's make sure that we can connect to the PostgreSQL server from our development machine by running the following command:

*Note: You'll need to substitute in your database user's values for [USERNAME], [PASSWORD], and [SERVER_IP].

> psql postgres://[USERNAME]:[PASSWORD]@[SERVER_IP]:80/sample -c "SELECT count(id) FROM employees;"
or
> psql "dbname=sample host=172.31.9.95 user=mikef password=pl@yn1ce port=80" --command "SELECT count(id) FROM employees;"

## Installing and Configuring the AWS CLI

The AWS CLI is written in Python and we can install it globally by exiting our virtualenv for a moment and running this command:
> exit
> pip3.7 install --user awscli

Next, we'll take the access key ID and secret access key that we copied before to configure out AWS client:
> aws configure

``` console
AWS Access Key ID [None]: XXXXXXXXXXXXXXXXXXXX
AWS Secret Access Key [None]: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Default region name [None]:
Default output format [None]:
That will create a ~/.aws directory that includes our default configuration and credentials.
```

## Creating Our S3 Bucket

From within the AWS Console, we need to create a new S3 bucket that we can use with our project. To do this, we need to search for "S3" in the services. Next, click "Create Bucket", give it a name, and use the default settings.

Once the bucket is created, we'll select it by name and go to the "Permissions" tab so that we can change a few things. From the "Permissions" tab, select the "Access Control List" sub-tab and then for "Public Access" allow "List objects".

Now we should be able to add items to our S3 bucket and make them publically readable to make things a little easier for us later.


## Manual Testing

Now that we've implemented our subprocess interaction, we'll take a moment to ensure that it actually works. We can load our entire project into the Python REPL by setting the PYTHONPATH environment variable to be our ./src directory:
>PYTHONPATH=./src python

``` py
 from pgbackup import pgdump
dump = pgdump.dump('postgres://demo:password@54.245.63.9:80/sample')
f = open('dump.sql', 'w+b')
f.write(dump.stdout.read())
f.close()
```

## Resources

Centos Package
https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm

Linux Academy Script for DB Creatation
https://raw.githubusercontent.com/linuxacademy/content-python-for-sys-admins/master/helpers/db_setup.sh

PostgreSQL - Ubuntu
https://help.ubuntu.com/community/PostgreSQL

Postgresql Org.
https://www.postgresql.org/docs/9.5/app-psql.html