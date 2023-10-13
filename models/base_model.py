#!/usr/bin/python3
"""BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
	"""BaseModel of the HBnB project."""

	def __init__(self, *args, **kwargs):
		"""BaseModel.

		Args:
			*args (any): value.
			**kwargs (dict): Key/value pairs of attributes.
		"""
		time_format = "%Y-%m-%dT%H:%M:%S.%f"
		self.id = str(uuid4())
		self.created_at = datetime.today()
		self.updated_at = datetime.today()
		if len(kwargs) != 0:
			for key, value in kwargs.items():
				if key == "created_at" or key == "updated_at":
					self.__dict__[key] = datetime.strptime(value, time_format)
				else:
					self.__dict__[key] = value
		else:
			models.storage.new(self)

	def save(self):
		"""add date to filestorage."""
		self.updated_at = datetime.today()
		models.storage.save()

	def to_dict(self):
		"""
		Return BaseModel dictionary
		"""
		diction = self.__dict__.copy()
		diction["created_at"] = self.created_at.isoformat()
		diction["updated_at"] = self.updated_at.isoformat()
		diction["__class__"] = self.__class__.__name__
		return diction

	def __str__(self):
		"""Return string"""
		string_repr = self.__class__.__name__
		return "[{}] ({}) {}".format(string_repr, self.id, self.__dict__)
