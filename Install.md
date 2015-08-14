Installation Prerequisites for Zeptat (Czech for: to ask)
=======================

Instructions for gems, databases and drivers.

*NB* Installation instructions are for Fedora 22


pdf parser docsplit prerequisites
------------------------
docsplit documentation:

      https://github.com/documentcloud/docsplit/


install on OS:

      dnf install poppler-utils poppler-data GraphicsMagick ghostscript tesseract libreoffice

install locally:

      gem install docsplit

MongoDB driver prerequisites
------------------------

      python3 -m pip install pymongo


Cassandra driver prerequisites
------------------------
To also allow for cassandra server usage

as root:

      pip install cassandra-driver

      pip install lz4

Must install snappy first see this link:

      https://code.google.com/p/snappy/

once installed, continue with python installations:

      pip install python-snappy

      pip install scales

      pip install blist

      dnf install gcc python-devel libev libev-devel



Installation setup for mongodb
------------------------
root install mongo:

        dnf install mongodb mongodb-server


To initiate MongoDB Database
------------------------
Create proper directory structure for mongodb:

        [root@localhost ~]# mkdir /data

        [root@localhost ~]# ln -s /home/matej/data/db /data/db

        [root@localhost ~]# ll /data/

        lrwxrwxrwx. 1 root root 19 Jul  2 10:52 db -> /home/matej/data/db

        [root@localhost ~]# chown -R matej:matej /data/

        [root@localhost ~]# ll /data/

        lrwxrwxrwx. 1 matej matej 19 Jul  2 10:52 db -> /home/matej/data/db

Now start server in terminal:

        mongod

Installation setup for Cassandra
------------------------
See: http://docs.datastax.com/en/cassandra/2.1/cassandra/install/installRHEL_t.html

Add the DataStax Community repository to the /etc/yum.repos.d/datastax.repo:

    [datastax]
    name = DataStax Repo for Apache Cassandra
    baseurl = http://rpm.datastax.com/community
    enabled = 1
    gpgcheck = 0

Install the packages:

      dnf install dsc21

      dnf install cassandra21-tools

To initiate Cassandra Database
------------------------

check to make sure these directories exist

* /var/log/cassandra
* /var/lib/cassandra

fix permission so can write to the above directories and
start cassandra in separate terminal:

      cassandra -f

Installation setup for PostgreSQL
------------------------

as root:

      dnf install postgresql postgresql-server postgresql-contrib postgresql-libs postgres-devel

start server at boot:

      systemctl enable postgresql

initialize postgres:

      [root@localhost ~]# postgresql-setup --initdb

should see this:

       * Initializing database in '/var/lib/pgsql/data'

       * Initialized, logs are in /var/lib/pgsql/initdb_postgresql.log

start postgres:

      systemctl start postgresql

switch to default user:

      su – postgres

      psql

Drivers for SQL Postgres and Python
------------------------
as root:

      pip install psycopg2





