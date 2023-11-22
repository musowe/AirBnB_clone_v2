#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

storage = FileStorage()
storage.reload()
