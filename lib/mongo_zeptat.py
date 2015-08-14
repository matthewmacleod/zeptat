import sys
import datetime
import pymongo
from pymongo import MongoClient


class Mongo_Zeptat(object):
    """ Simple class for using Mongo Database """
    client = None
    db = None
    coll = None
    db_name = 'zeptat'
    coll_name = 'ebooks'

    def init_database(self):
        print "Initializing database..."
        try:
            self.client = MongoClient('localhost', 27017)
            self.db = self.client[self.db_name]
            self.coll = self.db[self.coll_name]
            print "Initialized database."
        except pymongo.errors.ConnectionFailure, e:
            print "Could not connect to MongoDB: %s" % e

    def load_data(self):
        """ Loads data from files_to_upload, right now drop previous collection """
        print "Loading files to database..."
        self.client[self.db_name].drop_collection(self.coll_name)
        with open('files_to_upload') as f:
            for text in f:
                with open('texts/'+text.rstrip()) as t:
                    lines = []
                    for index, text_line in enumerate(t):
                        lines.append((index,text_line.rstrip()))
                    doc = { "title": text.rstrip(),
                            "lines": lines,
                            "date": datetime.datetime.utcnow()}
                    self.coll.insert_one(doc)

    def query(self, search_term):
        print "Searching Mongo database for " + search_term
        with open('files_to_upload') as f:
            for text in f:
                print "searching text: ", text.rstrip()
                for edoc in self.coll.find({"title": text.rstrip() }):
                    elines = edoc["lines"]
                    for line in elines:
                        if search_term in line[1]:
                                print "Title: ", text.rstrip()[:25]+"...", " *** ", line


    def query_count(self, search_term):
        print "Searching Mongo database for " + search_term
        with open('files_to_upload') as f:
            for text in f:
                counts = 0
                for edoc in self.coll.find({"title": text.rstrip() }):
                    elines = edoc["lines"]
                    for line in elines:
                        if search_term in line[1]:
                            counts += 1
                if counts > 0:
                        print "Title: ", text.rstrip()[:25]+"..." , " *** Number of line matches: ",  counts


    def print_titles(self):
        for doc in self.coll.find():
            print doc

    def drop_collection(self):
        self.client[self.db_name].drop_collection(self.coll_name)

    def drop_database(self):
        self.client.drop_database(self.db_name)



if __name__ == '__main__':
    zeptat = Mongo_Zeptat()
    zeptat.init_database()
    if sys.argv[1] == 'upload':
        zeptat.load_data()

    if sys.argv[1] == 'query':
        with open('query_list') as ql:
            for q in ql:
                zeptat.query(q.rstrip())

    if sys.argv[1] == 'query_count':
        with open('query_list') as ql:
            for q in ql:
                zeptat.query_count(q.rstrip())

    if sys.argv[1] == 'drop':
        zeptat.drop_collection()

