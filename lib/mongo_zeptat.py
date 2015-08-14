import sys
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

  def drop_collection(self):
      self.client[self.db_name].drop_collection(self.coll_name)



if __name__ == '__main__':
    zeptat = Mongo_Zeptat()
    zeptat.create_database()
    zeptat.drop_collection()

