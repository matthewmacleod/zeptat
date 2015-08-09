Zeptat (Czech for: to ask)
=======================
goal find text in parsed e-books


Pdf parser Prerequisites
------------------------
install on OS:

        dnf install install poppler-utils poppler-data GraphicsMagick ghostscript tesseract tesseract-ocr pdftk libreoffice

        dnf install mongodb mongodb-server

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
create proper directories:

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

            rake upload > out

or:

            ruby main.rb upload files_to_upload


Step 4. query database for text:
As of now database queries are not case sensitive

    cat query_list

    linear

now type:

    rake query

or:

    ruby main.rb query query_list


Step 5. to clean database





To document
------------------------
rdoc -f darkfish

Todo
------------------------
* edit docsplit to output bson or something that we can upload to mongodb




