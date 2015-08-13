import psycopg2
import sys

class Zeptat(object):
    con = None
    cur = None
    db_name = 'zeptat'

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
            print 'Error %s' % e
            sys.exit(1)


    def close(self):
        self.cur.close()
        self.con.close()





if __name__ == '__main__':
  zeptat = Zeptat()
  zeptat.version()
  zeptat.close()

