#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""

import json
import models
from uuid import uuid4, UUID
from os import environ
import datetime
from sqlalchemy import String, Integer, Column, DateTime, ForeignKey, Table
from sqlalchemy import Float, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

datetime = datetime.datetime
now = datetime.now
strptime = datetime.strptime
Base = declarative_base()


class BaseModel:
    """attributes and functions for BaseModel class"""

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), unique=True, primary_key=True, nullable=False)
        created_at = Column(
            DateTime,
            default=datetime.utcnow(),
            nullable=False
        )
        updated_at = Column(
            DateTime,
            default=datetime.utcnow(),
            nullable=False
        )

    def __init__(self, *args, **kwargs):
        """instantiation of new BaseModel Class"""
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = now()

    def __set_attributes(self, d):
        """converts kwargs values to python class attributes"""
        if 'id' not in d:
            d['id'] = str(uuid4())
        if 'created_at' not in d:
            d['created_at'] = now()
        elif not isinstance(d['created_at'], datetime):
            d['created_at'] = strptime(d['created_at'], "%Y-%m-%d %H:%M:%S.%f")
        if 'updated_at' in d:
            if not isinstance(d['updated_at'], datetime):
                d['updated_at'] = strptime(d['updated_at'],
                                           "%Y-%m-%d %H:%M:%S.%f")
        if '__class__' in d:
            del d['__class__']
        self.__dict__ = d

    def __is_serializable(self, obj_v):
        """checks if object is serializable"""
        try:
            nada = json.dumps(obj_v)
            return True
        except:
            return False

    def bm_update(self, name, value):
        """updates instance with name and value"""
        setattr(self, name, value)
        self.save()

    def save(self):
        """updates attribute updated_at to current time"""
        self.updated_at = now()
        models.storage.new(self)
        models.storage.save()

    def to_json(self):
        """returns json representation of self"""
        bm_dict = {}
        for k, v in (self.__dict__).items():
            if (self.__is_serializable(v)):
                bm_dict[k] = v
            else:
                bm_dict[k] = str(v)
        bm_dict["__class__"] = type(self).__name__
        if "_sa_instance_state" in bm_dict:
            del bm_dict["_sa_instance_state"]
        return(bm_dict)

    def __str__(self):
        """returns string type representation of object instance"""
        cname = type(self).__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)

    def delete(self):
        """deletes the current instance from the storage __objects variable"""
        models.storage.delete(self)
