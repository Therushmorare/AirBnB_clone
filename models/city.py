#!/usr/bin/python3
"""City class."""
from models.base_model import BaseModel


class City(BaseModel):
	"""City.

	Attributes:
		state_id (str): State ID.
		name (str): City Name.
	"""

	state_id = ""
	name = ""
