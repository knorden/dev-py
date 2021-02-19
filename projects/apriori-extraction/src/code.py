import collections
import csv
import copy
import itertools
# from mlxtend.frequent_patterns import apriori
# from mlxtend.frequent_patterns import association_rules
from collections import Counter
from itertools import combinations
import numpy as np
import pandas as pd

# SRC_PATH = 'data/browsingdata_50baskets.txt'
# SRC_PATH = 'data/browsing-data.txt'
SRC_PATH = 'data/data-small.txt'
# SUPP = 100
# SUPP = 200
SUPP = 5

srcDATABASE = []
dictMONO = {}

# I. RAW DATA EXTRACTING AND CLEANSING
#
#   Regardless of which library I use to compute combinations later, I always need to parse in and
#   cleanse data as the the primilinary step. This is a must to ensure useable data.
#
with open(SRC_PATH) as inputFile:
    srcLine = csv.reader(inputFile, delimtmp_iter=' ')
    for everyList in srcLine:

        if '' in everyList:
            everyList.remove('')
        # create new internal db
        srcDATABASE.append(everyList)

        # for item in everyList:
        #     if item not in dictMONO:
        #         dictMONO[item] = 1
        #     dictMONO[item] += 1
print('done parsing and cleansing')


# II. FILTERING
#
#   This is the start of the main project.
#
arr = srcDATABASE

# A = np.array(arr)

# d = Counter()
# for subset in A:
#     if len(A) < 2:
#         continue
#     subset.sort()
#     for comb in combinations(subset, 2):
#         d[comb] += 1

# tmp_iter = 0
# a = d.most_common()
# output = []
# for i in range(0, 5):
#     for pair, freq in a:
#         if i == 5:
#             break
#         if freq > SUPP:
#             output.append((pair, freq))
#             i += 1


# arr = np.array(ARR)
output = []
# METHOD 1
#####################################################################
d = Counter()
for subset in arr:
    if len(arr) < 2:
        continue
    subset.sort()
    for comb in combinations(subset, 2):
        d[comb] += 1

tmp_iter = 0
a = d.most_common()
output = []
while tmp_iter < 5:
    for pair, freq in a:
        if tmp_iter == 5:
            break
        if freq > SUPP:
            output.append((pair,freq))
            tmp_iter += 1

# METHOD 2
#####################################################################
# counts = collections.defaultdict(int)
# for collab in arr:
#     collab.sort()
#     for pair in tmp_itertools.combinations(collab, 2):
#         counts[pair] +=1
# tmp_iter = 0
# while (tmp_iter < 5):
#     for pair, freq in counts.items():
#         if tmp_iter == 5:
#             break
#         if freq > SUPP:
#             output.append((pair,freq))
#             tmp_iter += 1


# for item in output:
#     print(item)

print('done')
