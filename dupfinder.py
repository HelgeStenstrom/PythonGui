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

def findDups(parentFolder):
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            try:
                file_hash = hashfile(path)
                # Add or append the file path
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
            except PermissionError:
                pass
    return dups

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
