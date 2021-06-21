# we need the os.walk method
# reference: https://www.tutorialspoint.com/python3/os_walk.htm
# in short, the method walk() generates the file names in a directory tree by
# walking the tree either top-down or bottom-up.
import os
import argparse


class ParserError(Exception):
    """subclassing Exception for any parsing errors"""
    pass


class SafeParser(argparse.ArgumentParser):
    """subclassing the default parser to overload the error message"""

    def error(self, message):
        raise ParserError()


def walkdir(path):
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            print(os.path.join(root, name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Parses the commandline arguments.')
    # parser = SafeParser()
    parser.add_argument("dir",  # creates attributes 'dir' for the Namespace Object
                        nargs='?',
                        default=argparse.SUPPRESS,  # object Namespace not created if no agurment
                        help="Enter given directory"
                        )

    try:
        args = parser.parse_args()  # except when no CL argument supplied
        walkdir(args.dir)
    # except AttributeError:
        # print("Directory is not specified")
    except AttributeError as no_dir:
        raise Exception("Directory is not specified") from no_dir

    # THIS IS VERY GOOD FOR DEBUGGING, WILL LET ME KNOW EXACTLY WHERE THE ERROR IS
    # try:
    #   args = parser.parse_args()  # no_args
    #   fpath = args.dir
    #   walkdir(fpath)
    # except ParserError as no_args:
    #   raise ParserError("Directory is not specified") from no_args
