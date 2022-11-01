#!/usr/bin/python3
'''Module for square class.
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A subclass of Rectangle.
    '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id})" +\
                f" {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        '''Gets size
        '''
        return self.width

    @size.setter
    def size(self, size):
        '''Sets size
        '''
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        '''Updates an instance.
        '''
        attrs = ['id', 'size', 'x', 'y']

        if len(args):
            for attr_idx in range(len(args)):
                setattr(self, attrs[attr_idx], args[attr_idx])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        '''Returns the dictionary representation of an instance.
        '''
        dct = dict(self.__dict__)
        dct2 = {}
        dct_cpy = dct.copy()
        for key in dct_cpy:
            if 'width' in key:
                dct2.update(size=dct[key])
                del dct[key]
            elif 'height' in key:
                del dct[key]
            elif 'x' in key:
                dct2.update(x=dct[key])
                del dct[key]
            elif 'y' in key:
                dct2.update(y=dct[key])
                del dct[key]

        dct.update(dct2)
        return dct
