#!/usr/bin/python3
"""
This module defines the HBNB console
"""

import cmd


class HBNBCommand(cmd.Cmd):
	"""
	The HBNBCommand class defines the HBNB command interpreter

	Args:
		prompt (str): command line prompt
	"""

	prompt = "(hbnb) "
	
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
