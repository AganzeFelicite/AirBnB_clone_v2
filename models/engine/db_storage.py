from sqlalchemy import create_engine
from os import getenv
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.review import Review
from models.state import State
from models.base_model import Base
from sqlalchemy.orm import scoped_session,  sessionmaker


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """this is the mysql class"""
    __engine = None
    __session = None

    def __init__(self):
        """initialise a new dbstorage"""

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True
                                      )
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
            return (new_dict)

    def new(self, obj):
        """adding the element to the current session"""
        self.__session.add(obj)

    def save(self):
        """commit the changes to the db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete the object from the db"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and make a new session"""
        Base.metadata.create_all(self.__engine)
        Session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session_fact)
        self.__session = Session

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.remove()
