#!/usr/bin/env python3

import shutil
import os
import sys

recurse = False
for arg in sys.argv:
    if arg == "-r":
        recurse = True
        sys.argv.remove(arg)

path = os.path.expanduser("~") + "/rm_trash/"
if not os.path.exists(path):
    os.mkdir(path)

if not os.path.exists(path + "path.log"):
    os.mknod(path + "path.log")

for file in sys.argv[1:]:
    if not os.path.exists(file):
        sys.stderr.write("rm.py: cannot remove '" + file + "': No such file or directory\n")
        continue

    if recurse == False:
        if os.path.isdir(file):
            sys.stderr.write("rm.py: cannot remove '" + file + "': Is a directory\n")
            continue

    token = file.split("/")[-1]
    if os.path.exists(path + token):
        isfile = os.path.isfile(path + token)
        if isfile == True:
            tokens = token.split(".")
            file_found = True
            counter = 1
            while file_found:
                file_path = path + tokens[0] + "-" + str(counter) + "." + tokens[1]
                file_found = os.path.exists(file_path)
                counter += 1
        else:
            file_found = True
            counter = 1
            while file_found:
                file_path = path + token + "-" + str(counter)
                file_found = os.path.exists(file_path)
                counter += 1
    else:
        file_path = path + token

    shutil.move(file, file_path)    
    with open(path + "path.log", "a") as f:
        f.write(file + " " + file_path.split("/").pop() + "\n")
