from cassandra.cluster import Cluster
import sys

class Cassandra_Zeptat(object):
    """ Simple class for interacting with cassandra database """
    cluster = None
    session = None

    def connect(self, host):
        """ connect with host, use ["127.0.0.1"] for localhost, host must be in list format"""
        self.cluster = Cluster(host)
        self.session = self.cluster.connect()
        print "Cluster: %s" % self.cluster.metadata.cluster_name
        for host in self.cluster.metadata.all_hosts():
            print "Host: %s" % host

    def close(self):
        self.cluster.shutdown()

    def create_schema(self):
        """ Creates Schema, note primary key is title since want to keep lines local with respect to each ebook """
        self.session.execute("CREATE KEYSPACE IF NOT EXISTS zeptat "
                             "WITH REPLICATION = { 'class': 'SimpleStrategy', "
                             "'replication_factor': 1 };")
        self.session.execute("CREATE TABLE IF NOT EXISTS "
                             "zeptat.ebooks (title TEXT, "
                             "line INT, line_content TEXT, "
                             "PRIMARY KEY(title, line));")

    def load_data(self):
        """ load data from file files_to_upload, where full path is given for each file """
        with open('files_to_upload') as f:
            for text in f:
                with open('texts/'+text.rstrip()) as t:
                     for index, text_line in enumerate(t):
                         # print text_line.rstrip(), " line ", index
                         cql_to_insert = "INSERT INTO zeptat.ebooks (title, line, line_content) VALUES ('{0}', {1}, '{2}');".format(text.rstrip(), index, text_line.rstrip())
                         self.session.execute(cql_to_insert)

    def query(self, desired_title, search_term):
        """ query substring term in desired title """
        cql_to_insert ="SELECT * FROM zeptat.ebooks WHERE title = '{0}';".format(desired_title)
        results = self.session.execute(cql_to_insert)
        for r in results:
            if search_term in r.line_content:
                try:
                    print "Title: ", r.title[:25]+"...", " *** line: ", r.line, " *** content:  ", r.line_content
                except:
                    print "unicode error"



if __name__ == '__main__':
  zeptat = Cassandra_Zeptat()
  zeptat.connect(["127.0.0.1"])

  # upload files in files_to_upload to Cassandra database
  if sys.argv[1] == 'upload':
      zeptat.create_schema()
      zeptat.load_data()

  # full text search on uploaded files for search terms found in query_list file
  if sys.argv[1] == 'query':
      with open('files_to_upload') as f:
          for text in f:
              with open('query_list') as ql:
                  for q in ql:
                     zeptat.query(text.rstrip(),q.rstrip())



  zeptat.close()



