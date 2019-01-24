#!/usr/bin/python3
"""module for use as base class
"""



class Base:
    """base class for use with other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiates the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries
        """
        return str(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a list of objects to a file as a JSON string
        """
        new_list = None
        cname = None
        for obj in list_objs:
            # clean up list for non sub elements
            # doesn't effect original copy
            if not issubclass(type(obj), Base):
                if new_list is None:
                    new_list = list_objs.copy()
                new_list.remove(obj)
            elif cname is None or cname != "Rectangle":
                cname = obj.__class__.__name__

        super_list = []
        if new_list is None:
            for ele in list_objs:
                super_list.append(ele.to_dictionary())
        else:
            for ele in new_list:
                super_list.append(ele.to_dictionary())
        if cname is None:  # default used when empty list
            cname = "Rectangle"
        write_str = cls.to_json_string(super_list)
        with open(cname + '.json', 'w', encoding='utf-8') as myFile:
            myFile.write(write_str)

    @staticmethod
    def from_json_string(json_string):
        """returns a list of dictionary objects evaluated from json string
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return eval(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a new instance of sub class using that class's
            -> update method after instantiating one instance.
        """
        new_inst = cls(1, 1)
        if new_inst is not None:
            new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """returns a list of all instances in class's file
        """
        cname = cls.__name__
        try:
            with open(cname + '.json', 'r', encoding='utf-8') as myFile:
                text = myFile.read()
        except:
            return []

        inst_list = []
        dict_list = cls.from_json_string(text)
        for ele in dict_list:
            inst_list.append(cls.create(**ele))
        return inst_list
