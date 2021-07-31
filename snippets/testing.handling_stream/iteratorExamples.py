# use of iterators
def getCourse(it):
    course = ""
    for c in it:
        if c == "-":
            return course
        else:
            course += c
    return course


i = iter("CptS355-CptS322-CptS321")
course1 = getCourse(i)
course2 = getCourse(i)
course3 = getCourse(i)

# Additional Iterator Examples

# Generates an infinite sequence of natural numbers
# class Naturals(object):
class Naturals:
    def __init__(self, init):
        self.current = init

    def __next__(self):
        result = self.current
        self.current += 1
        return result

    def __iter__(self):
        return self


# -------------------------------------------------------------

# Generates an  sequence of natural numbers from init to N (inclusive)
class NaturalsUptoN(object):
    def __init__(self, init, N):
        self.current = init
        self.N = N

    def __next__(self):
        if self.current > self.N:
            raise StopIteration
        result = self.current
        self.current += 1
        return result

    def __iter__(self):
        return self


# -------------------------------------------------------------

# Creates a copy of the input iterable object.
# Version 1
class copyIter(object):
    def __init__(self, it):
        self.input1 = it

    def __next__(self):
        try:
            self.current = self.input1.__next__()
        except:
            raise StopIteration
        return self.current

    def __iter__(self):
        return self


# Version 2
class copyIter2(object):
    def __init__(self, it):
        self.input1 = it
        try:
            self.current = self.input1.__next__()
        except:
            self.current = None

    def __next__(self):
        if self.current is None:
            raise StopIteration
        result = self.current
        try:
            self.current = self.input1.__next__()
        except:
            raise StopIteration
        return result

    def __iter__(self):
        return self


# Version 3
class copyIter3(object):
    def __init__(self, it):
        self.input1 = it
        self.current = self._getNextInput()

    def _getNextInput(self):
        try:
            current = self.input1.__next__()
        except:
            current = None
        return current

    def __next__(self):
        if self.current is None:
            raise StopIteration
        result = self.current
        self.current = self._getNextInput()
        return result

    def __iter__(self):
        return self


# it = copyIter3(iter([1,2,3,4,5,6]))
# print("First:", it.__next__())
# print("Second", it.__next__())
# for item in it:
#     print(item)
#     if item == 5:
#         break
# print("last:",it.__next__()) # print 6
# #print(it.__next__()) # raise the StopIteration exception

# -------------------------------------------------------------
# Generte an iterator which takes an iterator of strings and generates a sequence of strings
# where each string is the concatanation of consecutive strings from the input iterator.
# Example : concatConsecutive(iter(["CptS","355","CptS","322","done"]))
#           should return "CptS355", "CptS322", "done"


class concatConsecutive(object):
    def __init__(self, it):
        self.input1 = it
        self.current = self._getNextInput()

    def _getNextInput(self):
        try:
            current = self.input1.__next__()
        except:
            current = None
        return current

    def __next__(self):
        if self.current is None:
            raise StopIteration
        result = self.current
        self.current = self._getNextInput()
        if self.current is None:
            return result
        else:
            result += self.current
            self.current = self._getNextInput()
            return result

    def __iter__(self):
        return self


it = concatConsecutive(iter(["CptS", "355", "CptS", "322", "done"]))
for s in it:
    print("Next string: ", s)


# -------------------------------------------------------------
# generator example
def letters(start, finish):
    current = start
    while current <= finish:
        print("before yield")
        yield current
        print("after yield")
        current = chr(ord(current) + 1)


gLetters = letters("a", "d")
print(gLetters.__next__())

for a in gLetters:
    print(a)
list(gLetters)
