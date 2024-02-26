#!/usr/bin/python3
"""Module with class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle

    Attributes:
        size (int): size of a side of the square
        x (int): x coordinate of the square
        y (int): y coordinate of the square
        id (int): identity of the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square

        Args:
            size (int): size of a side of the square
            x (int, optional): x coordinate. Defaults to 0
            y (int, optional): y coordinate. Defaults to 0
            id (int, optional): defaults to None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter of the size

        Returns:
            int: size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter of the size

        Args:
            value (int): new size of the square

        Raises:
            TypeError: if value is not an int
            ValueError: if value <= 0
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of the square

        Args:
            *args (ints): new attribute values
                - 1st: id attribute
                - 2nd: size attribute
                - 3rd: x attribute
                - 4th: y attribute
            **kwargs (dict): new key/value pairs of attributes
        """
        if args and len(args) != 0:
            attrs = ["id", "size", "x", "y"]
            for i, a in enumerate(args):
                setattr(self, attrs[i], a)

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k in ["id", "size", "x", "y"]:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns dictionary representation of the square

        Returns:
            dict: dictionary representation
        """
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y

        return d

    def __str__(self):
        """Return string representation"""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__,
            self.id,
            self.x,
            self.y,
            self.size)
