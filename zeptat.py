from cassandra.cluster import Cluster

class Zeptat(object):
    cluster = None
    session = None

    def connect(self, host):
        self.cluster = Cluster(host)
        self.session = self.cluster.connect()
        print "Cluster: %s" % self.cluster.metadata.cluster_name
        for host in self.cluster.metadata.all_hosts():
            print "Host: %s" % host

    def close(self):
        self.cluster.shutdown()

    def create_schema(self):
        self.session.execute("CREATE KEYSPACE IF NOT EXISTS zeptat "
                             "WITH REPLICATION = { 'class': 'SimpleStrategy', "
                             "'replication_factor': 1 };")
        self.session.execute("CREATE TABLE IF NOT EXISTS "
                             "zeptat.ebooks (title TEXT, "
                             "line INT, line_content TEXT, "
                             "PRIMARY KEY(title, line));")

    def load_data(self):
        with open('files_to_upload') as f:
            for text in f:
                with open('texts/'+text.rstrip()) as t:
                     for index, text_line in enumerate(t):
                         # print text_line.rstrip(), " line ", index
                         txt_to_insert = "INSERT INTO zeptat.ebooks (title, line, line_content) VALUES ('{0}', {1}, '{2}');".format(text.rstrip(), index, text_line.rstrip())
                         self.session.execute(txt_to_insert)



if __name__ == '__main__':
  zeptat = Zeptat()
  zeptat.connect(["127.0.0.1"])
  zeptat.create_schema()
  zeptat.load_data()



  zeptat.close()



