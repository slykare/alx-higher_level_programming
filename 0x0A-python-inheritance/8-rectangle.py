#!/usr/bin/python3
'''
8-rectangle.py.
Inherits from BaseGeometry.
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Class Rectangle that inherits from BaseGeometry.
    Private instances attributes:
        - width
        - height
    '''

    def __init__(self, width, height):
        '''
        Initializing a Rectangle instance
        Args:
           Width: width of the Rectangle
           Height: height of the Rectangle
        '''

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
