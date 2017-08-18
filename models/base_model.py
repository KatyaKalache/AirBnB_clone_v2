#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""

import json
import models
from uuid import uuid4, UUID
from os import environ
import datetime
from sqlalchemy import String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sys

datetime = datetime.datetime
utcnow = datetime.utcnow
strptime = datetime.strptime

if environ.get('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """attributes and functions for BaseModel class"""

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60),
                    unique=True,
                    primary_key=True,
                    nullable=False)
        created_at = Column(
            DateTime,
            default=utcnow(),
            nullable=False
        )
        updated_at = Column(
            DateTime,
            default=utcnow(),
            nullable=False
        )

    def __init__(self, *args, **kwargs):
        """instantiation of new BaseModel Class"""
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = utcnow()

    def __set_attributes(self, kwargs):
        """converts kwargs values to python class attributes"""
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid4())
        if 'created_at' not in kwargs:
            kwargs['created_at'] = utcnow()
        elif not isinstance(kwargs['created_at'], datetime):
            kwargs['created_at'] = strptime(kwargs['created_at'],
                                            "%Y-%m-%d %H:%M:%S.%f")
        if 'updated_at' not in kwargs:
            kwargs['updated_at'] = utcnow()
        if 'updated_at' in kwargs:
            if not isinstance(kwargs['updated_at'], datetime):
                kwargs['updated_at'] = strptime(kwargs['updated_at'],
                                                "%Y-%m-%d %H:%M:%S.%f")
        if environ.get('HBNB_TYPE_STORAGE') != 'db' and '__class__' in kwargs:
            del kwargs['__class__']
        for attr, val in kwargs.items():
            setattr(self, attr, val)

    def __is_serializable(self, obj_v):
        """checks if object is serializable"""
        try:
            json.dumps(obj_v)
            return True
        except:
            return False

    def bm_update(self, name, value):
        """updates instance with name and value"""
        setattr(self, name, value)
        self.save()

    def save(self):
        """updates attribute updated_at to current time"""
        self.updated_at = utcnow()
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
