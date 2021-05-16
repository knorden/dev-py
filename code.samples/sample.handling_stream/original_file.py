debugging = True


def debug(*s):
    """debugging function."""
    if debugging:
        print(*s)


def inf_words():
    """generate an infinite stream of words. Each word is of length 4 chars.
    The fifth symbol is always a space."""
    current = "a"
    nextchar = chr(ord(current) + 1)
    n = 1
    # this is the core loop
    while True:
        yield current
        n += 1
        if n > 4:
            current = " "
            n = 0
        else:
            current = nextchar
            nextchar = chr(ord(nextchar) + 1)
            if nextchar > "z":
                nextchar = "a"


# strg = ""
# words = iter(ii)
# for w in words:
#     if w == ' ':
#         strg += w
#         break
#     strg += w
#     debug (w)

# def decodeThis(ttable, chunk):
#     word = ""
#     for c in chunk:
#         if c not in ttable:
#             word += c
#         else:
#             word += ttable[c]
#     return word


# class DecodeIter:
#     def __init__(self,tt, ii):
#         self.table = tt
#         self.input = ii.split()
#         self.length = len(self.input)
#         self.input = iter(self.input)

#     def __iter__(self):
#         return self.input

#     def __next__(self):
#         tmpString = ""
#         i = 0
#         while i < self.length:
#             tmpString = decodeThis(self.table, self.input[i])
#             yield tmpString
#             i += 1

# return self.words
# def __next__(self):
#     tmpStrg = ""
#     for w in self.input:
#         if w == ' ' or w == '':
#             break
#         tmpStrg += w
#     self.words = decodeThis(self.ttable, tmpStrg)
#     return self.words
# while True:
#     yield self.words[self.n]
#     self.words.pop()
# self.word.append(tmpStrg)
# while len(self.word) > 0:
#     for i in range(len(self.word)):
#         yield self.word[i]

# msg1 = DecodeIter(tt1, jj)
# m1 = []
# msg1.__next__()
# msg1.__next__()
# msg1.__next__()
# msg1.__next__()
# msg1.__next__()
# msg1.__next__()

# msg1 = DecodeIter(tt1, ii1)
# m1 = []
# for i in msg1:
#     m1.append(msg1.__next__())

# msg2 = DecodeIter(tt2, ii2)
# a1 = msg2.__next__()
# a2 = msg2.__next__()
# msg2 = "" + (i for i in msg2)

# words = DecodeIter(tt1, ii1)
# L = []
# aa = words.__next__()
# bb = words.__next__()


# graph = {'A':'B','B':'D','C':'G','D':'E','E':'C', 'F':'I','G':'B','H':None,'I':'H'}


# def getnextnode(graph, start):
#     '''yields the next node in the graph.'''
#     curr = start
#     while curr is not None:
#         a = ""
#         a += curr
#         debug("this is the next node:", a)
#         yield a
#         curr = graph[curr]
#         if start == curr:
#             start = None

# gg = getnextnode(graph, 'A')
# L = []
# nn1 = gg.__next__()
# nn2 = gg.__next__()
