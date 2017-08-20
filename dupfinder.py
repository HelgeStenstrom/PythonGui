# import tkinter as tk


class ExampleClass:

    def __init__(self):
        self.created = True


class MyCollection:

    def __init__(self):
        self.collection = []

    def add(self, item):
        self.collection += [item]

    def has(self, item):
        return item in self.collection
