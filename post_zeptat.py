import psycopg2
import sys

class Zeptat(object):
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
        try:
            """ create zeptat postgres schema, note will drop table if exists """
            print "Creating table..."
            sql = "DROP TABLE IF EXISTS {0}".format(self.table_name)
            self.cur.execute(sql)
            sql_table = "CREATE TABLE {0} (title TEXT PRIMARY KEY, line INT, line_content TEXT);".format(self.table_name)
            self.cur.execute(sql_table)
            self.con.commit()

        except psycopg2.DatabaseError, e:
            print 'Create table error %s' % e

    def load_data(self, ebook_data):
        try:
            inserts = "INSERT INTO {0} (title,line,line_content) Values (%s, %s, %s)".format(self.table_name)
            self.cur.executemany(insters, ebook_data)
            self.con.commit()

        except psycopg2.DatabaseError, e:
            print 'Load data error %s' % e



    def close(self):
        self.cur.close()
        self.con.close()





if __name__ == '__main__':
  zeptat = Zeptat()
  zeptat.version()

  if sys.argv[1] == 'upload':
      zeptat.create_table()



  zeptat.close()

