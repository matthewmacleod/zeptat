Zeptat (Czech for: to ask)
=======================

Project goals and notes
------------------------

 * primary goal: find text in parsed e-books via database
 * secondary goal: test various databases, eg:
    * MongoDB
    * Cassandra
    * PostgreSQL
 * tertiary goal: test some big data tools, eg:
    * hadoop
    * spark

Third-party tools required to run Zeptat code:

  * docsplit gem

Mongo implementations:
  * Pymongo driver

Cassandra implementation:
  * Cassandra Python driver

PostgreSQL implementation:
  * psycopg2 driver

*NB* Installation instructions are for Fedora 22

* Installation notes are in Install.md file



To run Zeptat with MongoDB
------------------------
To Parse:
Step 1.  put file paths of pdfs into file input,

make a list of files to upload, eg

             find /home/matej/ebooks/programming/cs/ai/machine_learning/ -name "*pdf" | grep pdf > input

or can make list from files in different locations:

             cat input

             /home/matej/develop/test/ruby/pdfs/efficient_learning_machines.pdf

             /home/matej/ebooks/programming/cs/ai/machine_learning/Emerging Paradigms in Machine Learning.pdf


Step 2. then run:

               rake parse

or in long form:

                ruby lib/parse.rb input


To upload:
Step 3. load files into database:

to generate list of files that we parsed,

        ls texts > files_to_upload

Or make file for uploads, files_to_upload

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

to get the results from a specific file, do this eg,

     rake query_title name='20-ml-tools.txt'

Note: the full name does **not** need to be given, only enough of the name to make it unique with respect to other titles in database


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
* add big data tools


