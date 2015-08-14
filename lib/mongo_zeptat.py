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

    def create_database(self):
        print "Initializing database..."
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[self.db_name]
        self.coll = self.db[self.coll_name]
        print "Initialized database."

    def load_data(self):
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

    def print_titles(self):
        for doc in self.coll.find():
            print doc


    def drop_collection(self):
        self.client[self.db_name].drop_collection(self.coll_name)

    def drop_database(self):
        self.client.drop_database(self.db_name)



if __name__ == '__main__':
    zeptat = Mongo_Zeptat()
    if sys.argv[1] == 'upload':
        zeptat.create_database()
        zeptat.load_data()

    if sys.argv[1] == 'query':
       print "searching..."

    if sys.argv[1] == 'drop':
        zeptat.drop_collection()

