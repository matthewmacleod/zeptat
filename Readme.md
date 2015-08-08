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




To run
------------------------
Step 1.  put file paths of pdfs into file:

              input


Step 2. then run:

               rake parse

todo:

Step 3. load files into database:

Step 4. query database for text:




To document
------------------------
rdoc -f darkfish

Todo
------------------------
* edit docsplit to output bson or something that we can upload to mongodb




