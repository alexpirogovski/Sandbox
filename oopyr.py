#!/usr/bin/env python

class Pyramid:
    'A class defining a pyramid'
    def __init__(self, char, layers):
        self.char = char
        self.layers = layers

    def __print_chars(self, ch, times):
        for i in range(0, times):
            print(ch),

    def draw(self):
        for j in range(0, self.layers):
            self.__print_chars(" ", self.layers - j - 1)
            self.__print_chars(self.char, j * 2 + 1)
            print("")
## End of class definition


p = Pyramid('*',10)
p.draw()









