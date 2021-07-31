import os
import time


def test_walk():
    # for root, dirs, files in os.walk(".", topdown=False):
    for root, dirs, files in os.walk(".", topdown=True):
        print("\n" + 60 * "--")
        print(f"ROOT: {root}\nDIRS: {dirs}\nFILES: {files}\n")
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
        time.sleep(8.0)
    pass


if __name__ == "__main__":
    test_walk()
