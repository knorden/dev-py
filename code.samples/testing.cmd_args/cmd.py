import sys


def session(this_session=True):
    assert this_session is True, "this_session must be True for program to run"
    filename = sys.argv[1]
    print(filename)


if __name__ == "__main__":
    session()

