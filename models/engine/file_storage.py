#!/usr/bin/python3
"""Import classes."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
	"""FileStorage class.
	Attributes:
		__file_path (str): The name of file path.
		__objects (dict): A dictionary.
	"""
	__file_path = "file.json"
	__objects = {}

	@property
	def file_path(self):
		return self.__file_path

	@property
	def objects(self):
		return self.__objects

	def all(self):
        	"""Return  __objects."""
        	return FileStorage.__objects

	def new(self, obj):
        	"""Set new"""
        	object_name = obj.__class__.__name__
        	FileStorage.__objects["{}.{}".format(object_name, obj.id)] = obj

	def save(self):
        	"""save method"""
        	storage = FileStorage.__objects
        	object_dictionary = {obj: storage[obj].to_dict() for obj in storage.keys()}
        	with open(FileStorage.__file_path, "w") as f:
            		json.dump(object_dictionary, f)

	def reload(self):
        	"""reload method."""
        	try:
            		with open(FileStorage.__file_path) as f:
                		object_dictionary = json.load(f)
                		for o in object_dictionary.values():
                    			cls_name = o["__class__"]
                    			del o["__class__"]
                    			self.new(eval(cls_name)(**o))
        	except FileNotFoundError:
            		return
