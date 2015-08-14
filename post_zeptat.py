import psycopg2
import sys

class Post_Zeptat(object):
    """ Simple class to interact with PostgreSQL server """
    con = None
    cur = None
    db_name = 'zeptat'
    table_name = 'ebooks'

    def version(self):
        """  Should return version information, eg:

          ('PostgreSQL 9.4.4 on x86_64-redhat-linux-gnu,
          compiled by gcc (GCC) 5.1.1 20150422 (Red Hat 5.1.1-1), 64-bit',)

          Note: database (db_name) must exist previous to running
        """
        print "Version number print out..."
        try:
            self.con = psycopg2.connect(database=self.db_name, user='postgres')
            self.cur = self.con.cursor()
            self.cur.execute('SELECT version()')
            ver = self.cur.fetchone()
            print ver

        except psycopg2.DatabaseError, e:
            print 'Version error %s' % e
            sys.exit(1)


    def create_table(self):
        """ create zeptat postgres schema, note will drop table if exists """
        try:
            print "Creating table..."
            sql = "DROP TABLE IF EXISTS {0}".format(self.table_name)
            self.cur.execute(sql)
            sql_table = "CREATE TABLE {0} (id INTEGER PRIMARY KEY, title TEXT, line INT, line_content TEXT);".format(self.table_name)
            self.cur.execute(sql_table)
            self.con.commit()

        except psycopg2.DatabaseError, e:
            print 'Create table error %s' % e


    def load_data(self):
        """ load data expects the data to upload in form of a tuple of tuples """
        try:
            with open('files_to_upload') as f:
                i = 0
                for text in f:
                    with open('texts/'+text.rstrip()) as t:
                        for index, text_line in enumerate(t):
                            sql_insert = "INSERT INTO {0} (id, title, line, line_content) Values ({1}, '{2}', {3}, '{4}')".format(self.table_name, i, text.rstrip(), index, text_line.rstrip())
                            self.cur.execute(sql_insert)
                            i += 1

            self.con.commit()

        except psycopg2.DatabaseError, e:
            if self.con:
                self.con.rollback()

            print 'Load data error %s' % e


    def query(self, search_term):
        print "Searching for text: {0} ...".format(search_term)
        try:
            sql_query = "SELECT * FROM {0}".format(self.table_name)
            self.cur.execute(sql_query)
            rows = self.cur.fetchall()
            for row in rows:
                if search_term in row[3]:
                    print row[1][:25] + "...", row[2], row[3]

        except psycopg2.DatabaseError, e:
            print 'Query error %s' % e


    def close(self):
        self.cur.close()
        self.con.close()





if __name__ == '__main__':
  zeptat = Post_Zeptat()
  zeptat.version()

  if sys.argv[1] == 'upload':
      zeptat.create_table()
      zeptat.load_data()

  if sys.argv[1] == 'query':
      with open('query_list') as ql:
          for q in ql:
              zeptat.query(q.rstrip())



  zeptat.close()

