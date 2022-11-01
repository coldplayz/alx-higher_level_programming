#!/usr/bin/python3
'''Module for class Base.
'''
import json


class Base:
    '''The base class of the project.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if type(id) is not int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def load_from_file(cls):
        try:
            with open(f"{cls.__name__}.json", 'r', encoding='utf-8') as fin:
                s = fin.read()
                dct_list = cls.from_json_string(s)
                inst_list = []
                for dct in dct_list:
                    inst_list.append(cls.create(**dct))
                return inst_list
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        try:
            with open(f"{cls.__name__}.csv", 'r', encoding='utf-8') as fin:
                s = fin.read()
                dct_list = cls.from_json_string(s)
                inst_list = []
                for dct in dct_list:
                    inst_list.append(cls.create(**dct))
                return inst_list
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        try:
            # For Square class; first argument is for size attribute...
            # ...if an exception is raised, it indicates cls is Rectangle
            inst = cls(1, 0)
        except ValueError:
            # For Rectangle class, as second argument should also be > 0
            inst = cls(1, 1)
        inst.update(**dictionary)
        return inst

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(f"{cls.__name__}.json", 'w', encoding='utf-8') as fout:
            s = []
            if list_objs is not None:
                for obj in list_objs:
                    if isinstance(obj, Base):
                        s.append(cls.to_dictionary(obj))
            s = cls.to_json_string(s)
            fout.write(s)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open(f"{cls.__name__}.csv", 'w', encoding='utf-8') as fout:
            s = []
            if list_objs is not None:
                for obj in list_objs:
                    if isinstance(obj, Base):
                        s.append(cls.to_dictionary(obj))
            s = cls.to_json_string(s)
            fout.write(s)

    @classmethod
    def reset_nb(cls):
        Base.__nb_objects = 0
