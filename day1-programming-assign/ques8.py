#!/usr/bin/python3

class Rectangle(object):

    def __init__(self,length=1,width=1):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

rect = Rectangle(25,3)
print(rect.area())
