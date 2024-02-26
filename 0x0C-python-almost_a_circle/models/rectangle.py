#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''A class representing a rectangle.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor method for Rectangle.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Getter method for the width of the rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter method for the width of the rectangle.'''
        self.check_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Getter method for the height of the rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter method for the height of the rectangle.'''
        self.check_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''Getter method for the x-coordinate of the rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter method for the x-coordinate of the rectangle.'''
        self.check_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''Getter method for the y-coordinate of the rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter method for the y-coordinate of the rectangle.'''
        self.check_integer("y", value)
        self.__y = value

    def check_integer(self, name, value, eq=True):
        '''Validates if the given value is an integer and meets specific criteria.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''Computes the area of the rectangle.'''
        return self.width * self.height

    def display(self):
        '''Prints a visual representation of the rectangle.'''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        '''Returns a string representation of the rectangle.'''
        return '[{}] ({}) {}/{} - {}/{}'.format(
            type(self).__name__, self.id, self.x, self.y, self.width, self.height
        )

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal method to update instance attributes via positional or keyword arguments.'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via positional and keyword arguments.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns a dictionary representation of the rectangle.'''
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
