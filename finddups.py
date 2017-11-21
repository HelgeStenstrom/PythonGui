#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Find duplicate files by walking a directory structure,
# find files of same size and then
# find files with the same md5 sum (but only if the size is the same)

# TODO: make compatible with python3. There are unicode problems.

import argparse
import os
# import md5
import hashlib


def getFileList(start_dir):
    file_list = []

    for root, dirs, files in os.walk(start_dir):
        for name in files:
            fullname = os.path.join(root, name)
            file_list += [fullname]
    return file_list


def dictOfSizes(file_list):
    sizes = [(os.stat(filename).st_size, filename) for filename in file_list]

    d = {}
    for f in sizes:
        try:
            d[f[0]] += [f[1]]
        except KeyError:
            d[f[0]] = [f[1]]
    return d


def sieveSameSize(d):
    dd = {}
    for item in d:
        count = len(d[item])
        if count != 1:
            dd[item] = d[item]
    return dd


def myMd5(filename):
    m = hashlib.md5()
    f = open(filename).read()
    m.update(f)
    return m.hexdigest()


def sameMd5(files):
    """Returns true if all items in the list are equal."""
    hashes = [myMd5(file) for file in files]
    hashes.sort()
    return hashes[0] == hashes[-1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("start", help="directory to start the search from")
    args = parser.parse_args()
    start_dir = args.start
    print("Starting search from %s" % start_dir)
    fl = getFileList(start_dir)
    dd = dictOfSizes(fl)
    dd2 = sieveSameSize(dd)
    for size in dd2:
        if sameMd5(dd2[size]):
            print("%s: %g duplicates" % (dd2[size][0], len(dd2[size])))


if __name__ == "__main__":
    main()
