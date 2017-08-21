# import tkinter as tk


class ExampleClass:

    def __init__(self):
        self.created = True

class File:
    def __init__(self, file):
        pass

class MyCollection:

    def __init__(self):
        self.collection = []

    def add(self, item):
        self.collection += [item]

    def has(self, item):
        return item in self.collection
