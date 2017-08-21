# import tkinter as tk
import hashlib
import os

def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

class ExampleClass:

    def __init__(self):
        self.created = True

class File:
    def __init__(self, file):
        self.thelength = os.path.getsize(file)

    def length(self):
        return self.thelength

class MyCollection:

    def __init__(self):
        self.collection = []

    def add(self, item):
        self.collection += [item]

    def has(self, item):
        return item in self.collection
