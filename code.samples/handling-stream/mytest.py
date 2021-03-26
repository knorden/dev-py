"""Working on the class object to handle stream input
"""
import inputs as ai


# debugging flag
DEBUGGING = True


def debug(*s):
    """DEBUGGING function."""
    print(*s) if DEBUGGING else None


# Setting up input variables
ii2, tt2 = ai.input2, ai.ttable2

# testing the debugging function above.
# debug("this is me testing the debug function:", DEBUGGING)


# def decode_this(table, chunk):
#     '''decoder function. looks up key and return decoded value.'''
#     word = ""
#     for c in chunk:
#         if c in table:
#             word += table[c]
#         else:
#             word += c
#     return word


def decode_this(table, chunk):
    '''decoder function. looks up key and return decoded value.'''
    word = ""
    for c in chunk:
        word += table.get(c, c)
    return word


class ConcatConsecutive:
    """A test class to handle input stream."""

    def __init__(self, tt, someInput):
        """Constructor."""
        self.table = tt
        self.itr_input = someInput
        self.current = self._get_next_input()
        self.result = ""

    def _get_next_input(self):
        """Handles the parsing of input."""
        try:
            self.current = self.itr_input.__next__()
            tmp = decode_this(self.table, self.current)
            self.current = tmp
        # exception handling for None input
        except StopIteration:
            self.current = None
            raise StopIteration from None
        return self.current

    def __iter__(self):
        return self

    def __next__(self):
        # if self.current is None:
        #     raise StopIteration
        while ' ' not in self.current:
            self.result += self.current
            self.current = self._get_next_input()
            if self.current is None:
                return self.result

            self.result += self.current
            self.current = self._get_next_input()
        result = self.result
        self.current = self._get_next_input()
        self.result = ""
        return result


# it = ConcatConsecutive(iter(["CptS", "355", "CptS", "322", "done"]))


def testFunc(itr):
    for i in range(20):
        out = itr.__next__()
        print("Next string: ", out)


ii = ConcatConsecutive(tt2, ii2)

testFunc(ii)
