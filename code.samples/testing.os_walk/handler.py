# we need the os.walk method
# reference: https://www.tutorialspoint.com/python3/os_walk.htm
# in short, the method walk() generates the file names in a directory tree by
# walking the tree either top-down or bottom-up.
import os
import argparse


def walk_it(path):
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files: 
            print(os.path.join(root, name))


if __name__ == "__main__":
    cmd_parser = argparse.ArgumentParser(description='Parses the commandline arguments.')
    cmd_parser.add_argument("", help='the full path is required.')
    args = cmd_parser.parse_args()
    fpath = args.file

    walk_it(fpath)
