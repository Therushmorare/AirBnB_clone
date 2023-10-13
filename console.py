#!/usr/bin/python3
"""
This module defines the HBNB console
"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from parse_func import parse

class HBNBCommand(cmd.Cmd):
	"""
	The HBNBCommand class defines the HBNB command interpreter

	Attributes:
		prompt (str): command line prompt
	"""

	prompt = "(hbnb) "
	__classes = {'BaseModel': BaseModel, 'User': User, 'City': City,'Place': Place, 'Amenity': Amenity, 'Review': Review,'State': State}
	
	def do_quit(self, arg):
		"""
		Quit command to exit the program
		"""
		return True

	def do_EOF(self, arg):
		"""
		EOF command to exit the program
		"""
		print("")
		return True

	def do_create(self, arg):
		"""
		Create function
		"""
		argument = parse(arg)
		if len(argument) == 0:
			print("** class name missing **")
		elif argument[0] not in HBNBCommand.__classes:
			print("** class doesn't exist **")
		else:
			print(eval(argument[0])().id)
			storage.save()

	def do_show(self, arg):
		"""
		Show function
		"""
		argument = parse(arg)
		object_dictionary = storage.all()
		if len(argument) == 0:
			print("** class name missing **")
		elif argument[0] not in HBNBCommand.__classes:
			print("** class doesn't exist **")
		elif len(argument) == 1:
			print("** instance id missing **")
		elif "{}.{}".format(argument[0], argument[1]) not in object_dictionary:
			print("** no instance found **")
		else:
			print(object_dictionary["{}.{}".format(argument[0], argument[1])])


if __name__ == '__main__':
   	HBNBCommand().cmdloop()
