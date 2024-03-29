#!/usr/bin/python3
"""
Module 10-square.py
iherits from Rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """inherits from class Rectangle"""

    def __init__(self, size):
        """initialization"""

        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """implements area method and return area"""
        return self.__size ** 2
