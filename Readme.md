Efind
=======================
goal find text in parsed e-books


Pdf parser Prerequisites
------------------------
install on OS:

yum install install poppler-utils poppler-data GraphicsMagick ghostscript tesseract tesseract-ocr pdftk libreoffice

install locally:

gem install docsplit

MongoDB Prerequisites
------------------------
gem update --system
gem install mongo
gem install bson
gem install bson_ext




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


