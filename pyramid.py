#!/usr/bin/env python

layers = input("Enter number of layers:")

layers = int(layers)


def print_chars(char, times):
    for i in range(0, times):
        print(char, end=" ")  # comma at the end not needed in py3 \n


for j in range(0, layers):
    print_chars(" ", layers - (j + 1))
    print_chars("*", j * 2 + 1)
    print("")
