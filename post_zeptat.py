import psycopg2
import sys

class Zeptat(object):
    con = None
    db_name = 'zeptat'

    def version(self):
        try:
            # note that datbase must exist previous to running
            self.con = psycopg2.connect(database=self.db_name, user='postgres')
            cur = self.con.cursor()
            cur.execute('SELECT version()')
            ver = cur.fetchone()
            print ver

        except psycopg2.DatabaseError, e:
            print 'Error %s' % e
            sys.exit(1)


    def close(self):
        self.con.close()





if __name__ == '__main__':
  zeptat = Zeptat()
  zeptat.version()
  zeptat.close()

