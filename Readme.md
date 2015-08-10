Zeptat (Czech for: to ask)
=======================

Project goal is to find text in parsed e-books via database

Third-party Tools required to run Zeptat code: ruby, docsplit gem, mongo driver, mongodb

Pdf parser Prerequisites
------------------------
docsplit documentation:

       https://github.com/documentcloud/docsplit/


install on OS:

        dnf install poppler-utils poppler-data GraphicsMagick ghostscript tesseract libreoffice

install locally:

          gem install docsplit

MongoDB Prerequisites
------------------------
          gem update --system

          gem install mongo

          gem install bson

          gem install bson_ext

          gem install json



setup mongodb
------------------------
root install mongo:

        dnf install mongodb mongodb-server

create proper directory structure for mongodb:

        [root@localhost ~]# mkdir /data

        [root@localhost ~]# ln -s /home/matej/data/db /data/db

        [root@localhost ~]# ll /data/

        lrwxrwxrwx. 1 root root 19 Jul  2 10:52 db -> /home/matej/data/db

        [root@localhost ~]# chown -R matej:matej /data/

        [root@localhost ~]# ll /data/

        lrwxrwxrwx. 1 matej matej 19 Jul  2 10:52 db -> /home/matej/data/db

now start server in terminal:

        mongod




To Run:
------------------------
To Parse:
Step 1.  put file paths of pdfs into file input,


             cat input

             /home/matej/develop/test/ruby/pdfs/efficient_learning_machines.pdf

             /home/matej/ebooks/programming/cs/ai/machine_learning/Emerging Paradigms in Machine Learning.pdf


Step 2. then run:

               rake parse

or in long form:

                ruby main.rb parse input


To upload:
Step 3. load files into database:
fix file for uploads, files_to_upload

eg,

          cat files_to_upload

          efficient_learning_machines.txt

          Emerging Paradigms in Machine Learning.txt


Now run:

            rake upload > out.txt

or:

            ruby main.rb upload files_to_upload clean_boolean

where clean_boolean is either true or false, where true drops current zeptat database before uploading new files.
The default (ie when use rake upload) is to drop current zeptat database, use long form if do not want this behaviour.


Step 4. query database for text:
As of now database queries are *not* case sensitive, eg:

    cat query_list

    linear

now type:

    rake query

or:

    ruby main.rb query query_list

Step 5. get counts of line matches for each title:

use query file eg:

      cat query_list

      svm


now type:

      rake query_count


To clean database
------------------------
to drop database:

     rake clean





To document
------------------------
rdoc -f darkfish

Todo
------------------------
* add additional query flexibility
* add query_count



