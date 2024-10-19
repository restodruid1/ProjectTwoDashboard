from pymongo import MongoClient
from bson.objectid import ObjectId

class animalShelter(object):

	def __init__(self,username,password):
		USER = username #'aacuser'
		PASS = password #'snhu1234'
		HOST = 'nv-desktop-services.apporto.com'
		PORT = 30770
		DB = 'AAC'
		COL = 'animals'
		
		self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
		self.database = self.client['%s' % (DB)]
		self.collection = self.database['%s' % (COL)]
		
	
	def create(self, data={}):
		if data != {}:
			try:
				result = self.database.animals.insert_one(data)
				return True
			except PyMongoError as e:
				#print("Error: ", e)
				return False
				
		else:
			#raise Exception("Nothing to save, because data parameter is empty")
			return False
			
	
	def read(self, data={}):
		if data is not None:
			try:
				result = list(self.database.animals.find(data))
				return result
			except PyMongoError as e:
				#print("Error: ", e)
				return []
							
		else:
			#raise Exception("Nothing to save, because data parameter is empty")
			return []
			
	
	def update(self, dataIn={}, changes={}):
		if dataIn != {}:			
			try:
			# Update data in database
				updateData = self.database.animals.update_one(dataIn, {'$set': changes})
				return updateData.modified_count
				
			except PyMongoError as e:
				print("Error: ", e)
				return 0
		else:
			return 0
		
	
	def delete(self, deleteData={}):
		if deleteData != {}:
			try:
			#Delete data from database
				result = self.database.animals.delete_one(deleteData)
				return result.deleted_count
			except PyMongoError as e:
				print("Error: ", e)
				return 0
							
		else:
			print("Could Not Find Data")
			return 0
