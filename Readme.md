Zeptat (Czech for: to ask)
=======================

Project goals and notes
------------------------

 * primary goal: to find text in parsed e-books via database
 * secondary goal: test various databases:
    * MongoDB
    * Cassandra
    * PostgreSQL


Third-party tools required to run Zeptat code:

  * docsplit gem

Mongo implementations:
  * Pymongo driver

Cassandra implementation:
  * Cassandra Python driver

PostgreSQL implementation:
  * psycopg2 driver

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

      pip install pymongo


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





To run Zeptat with MongoDB
------------------------
To Parse:
Step 1.  put file paths of pdfs into file input,


             cat input

             /home/matej/develop/test/ruby/pdfs/efficient_learning_machines.pdf

             /home/matej/ebooks/programming/cs/ai/machine_learning/Emerging Paradigms in Machine Learning.pdf


Step 2. then run:

               rake parse

or in long form:

                ruby lib/parse.rb input


To upload:
Step 3. load files into database:
fix file for uploads, files_to_upload

eg,

          cat files_to_upload

          efficient_learning_machines.txt

          Emerging Paradigms in Machine Learning.txt


Now run:

            rake upload



Step 4. query database for text:
As of now database queries are *not* case sensitive, eg:

    cat query_list

    linear

now type:

    rake query

or:



abridged example output:

      Title: elements_of_statistical_learning_Hastie2009 *** line number: 102 Path algorithm for SVM classifier

      Title: elements_of_statistical_learning_Hastie2009 *** line number: 819 12.3.1 Computing the SVM for Classification . . . . .

      Title: elements_of_statistical_learning_Hastie2009 *** line number: 820 12.3.2 The SVM as a Penalization Method . . . . . .

      Title: elements_of_statistical_learning_Hastie2009 *** line number: 822 12.3.4 SVMs and the Curse of Dimensionality . . . .

      Title: elements_of_statistical_learning_Hastie2009 *** line number: 823 12.3.5 A Path Algorithm for the SVM Classifier . . .


Step 5. get counts of line matches for each title:

use query file eg:

      cat query_list

      svm


now type:

      rake query_count

abridged example output:


      Title: efficient_learning_machines                    *** Number of line matches: 234.0

      Title: elements_of_statistical_learning_Hastie2009    *** Number of line matches: 58.0

      Title: Emerging Paradigms in Machine Learning         *** Number of line matches: 152.0


To clean database
------------------------
to drop Mongo database:

     rake drop



To run Zeptat with Cassandra
------------------------
To upload files in files_to_upload run:

      rake upload_cassandra

To query terms in file query_list run:

      rake query_cassandra



To run Zeptat with PostgreSQL
------------------------
To upload files in files_to_upload run:

      rake upload_postgres

To query terms in file query_list run:

      rake query_postgres



To document
------------------------
rdoc -f darkfish

Todo
------------------------
* add additional mongo query flexibility



