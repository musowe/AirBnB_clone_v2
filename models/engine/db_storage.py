"""new class for sqlAlchemy"""
from os import getenv

from sqlalchemy import create_engine

from models.amenity import Amenity
from models.base_model import Base
from models.place import Place
from models.review import Review
from models.state import City, State
from models.user import User


class DBStorage:
    """creates tables in environment"""

    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            "mysql+mysqldb://{user}:{passwd}@{host}/{db}", pool_pre_ping=True
        )
