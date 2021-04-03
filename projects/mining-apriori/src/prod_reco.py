import csv
import copy

# inPath = 'data/browsingdata_50baskets.txt'      # (test) small set
inPath = 'data/browsing-data.txt'              # real set

# s = 5       # support threshold for the small dataset (test)
s = 100   # support threshold for the large dataset
# s = 200   # support threshold for the large dataset

originDATABASE = []
dictMONO = {}
# I. PARSING AND CLEANING DATA
#
# Parses and cleans data from the source input. This operation combines together the following two
# operations to avoid frequent I/O actions:
#   - creating a mirror image of the source input.
#   - building a dictionary of all single-item sets.

with open(inPath) as inputFile:
    # with open('data/data-big.txt') as inputFile:
    src_line = csv.reader(inputFile, delimiter=' ')
    for itemList in src_line:

        # Filter out non-data:
        if '' in itemList:
            itemList.remove('')

        # Gathers data into local database to reduce I/O operations on the source:
        originDATABASE.append(itemList)

        # Builds a dictionary of single-item entries:
        for item in itemList:
            if item not in dictMONO:
                dictMONO[item] = 1
            dictMONO[item] += 1
print("done parsing and cleaning")


# II. FILTERING DATA & BUILDING CANDIDATE DATABASE & EXTRACTING QUALIFIED PAIRS
#
# A. FILTERING:
#    From the monoset dictionary, EXTRACT only entries that pass the threshold s=100,
#    because an item that does not pass 100 counts is NOT frequent, thus all of its supersets
#    would NOT be frequent.
thresholdDICT = {}
for key in dictMONO:
    if dictMONO[key] > s:
        thresholdDICT[key] = dictMONO[key]
#
# B. BUILDING CANDIDATE DATABASE:
dictPAIR = {}
pairCANDIDATES = []
for line in originDATABASE:
    if not line:
        continue
    clone1 = copy.deepcopy(line)
    isFrequentLine = 0
    for a in line:
        clone1.remove(a)
        for b in clone1:
            # if b not in dictMONO:
            if b not in thresholdDICT:
                continue
            if frozenset([a, b]) not in dictPAIR:
                dictPAIR[frozenset([a, b])] = 1
                isFrequentLine += 1
            elif frozenset([a, b]) in dictPAIR:
                dictPAIR[frozenset([a, b])] += 1
                isFrequentLine += 1
    if isFrequentLine > 0:
        pairCANDIDATES.append(line)
print("done building pair-Candidates")
#
# C. EXTRACTING ONLY PAIRS THAT PASS THE SUPPORT THRESHOLD:
dictPAIRpass = {}
for key in dictPAIR:
    if dictPAIR[key] > s:
        dictPAIRpass[key] = dictPAIR[key]
print("done with pairs")

sortedDICT = {}
sortedKeys = sorted(dictPAIRpass, key=dictPAIRpass.get, reverse=True)
for key in sortedKeys:
    sortedDICT[key] = dictPAIRpass[key]
print("done sorting dict")

outputList = []
# Gets the confidence
i = 0
for pair in sortedDICT:
    outlist = {}
    if i == 5:
        break
    i += 1
    for item in pair:
        itemSUPP = dictMONO[item]
        pairSUPP = dictPAIR[pair]
        confidence = pairSUPP / itemSUPP
        outlist[item] = confidence
    outputList.append(outlist)
print("done getting output")

sortedTopFive = []
for pair in outputList:
    outlist = []
    keymax = max(pair, key=pair.get)
    outlist.append(keymax)
    for element in pair:
        if element is not keymax:
            outlist.append(element)
            break
    outlist.append(pair[keymax])
    sortedTopFive.append(outlist)
print("done another")

with open("output.txt", 'w') as outputFile:
    outputFile.write("OUTPUT A\n")   
    for list in sortedTopFive:
        outstr = ''
        outstr = " ".join([str(elem) for elem in list])
        outstr += "\n"
        outputFile.write(outstr)


# III. REPEAT II. FOR TRIPLETS:
#
# A. From previous process
#
# B. BUILDING CANDIDATE DATABASE:
dictTRES = {}
tripletCANDIDATES = []
# for line in originDATABASE:
for line in pairCANDIDATES:
    if not line:
        continue
    clone1 = copy.deepcopy(line)
    for a in line:
        clone1.remove(a)
        for b in clone1:
            clone2 = copy.deepcopy(clone1)
            clone2.remove(b)
            clone3 = copy.deepcopy(line)
            if frozenset([a,b]) not in dictPAIRpass:
                continue
            for c in clone3:
                if c == a or c == b:
                    continue
                if frozenset([a, b, c]) not in dictTRES:
                    dictTRES[frozenset([a, b, c])] = 1
                elif frozenset([a, b, c]) in dictTRES:
                    dictTRES[frozenset([a, b, c])] += 1
print("done building triplet-Candidates")
#
# C. EXTRACTING QUALIFIED PAIRS:
dictTRESpass = {}
for key in dictTRES:
    if dictTRES[key] > s:
        dictTRESpass[key] = dictTRES[key]
print("done with triplets")

sortedDICT = {}
sortedKeys = sorted(dictTRESpass, key=dictTRESpass.get, reverse=True)
for key in sortedKeys:
    sortedDICT[key] = dictTRESpass[key]
print("done sorting dict")

outputList = []
# get confidence
i = 0
for triplet in sortedDICT:
    outlist = {}
    if i == 5:
        break
    i += 1
    for elem in triplet:
        tmp = []
        tmp.append(elem)
    for elem in triplet:
        if elem:
            tmp2 = copy.deepcopy(tmp)
            tmp2.remove(elem)
        # for item in tmp2:
        #     if frozenset([elem, item]) in dictPAIRpass:
    for item in triplet:
        itemSUPP = dictMONO[item]
        tripletSUPP = dictTRES[triplet]
        confidence = tripletSUPP / itemSUPP
        outlist[item] = confidence
    outputList.append(outlist)
print("done getting output")


sortedTopFive = []
for triplet in outputList:
    outlist = []
    tmp = []
    for element in triplet:
        if triplet[element] > 1:
            continue
        tmp.append(element)
    if max(tmp):
        keymax = max(tmp)
    outlist.append(keymax)
    for element in triplet:
        if element is not keymax:
            outlist.append(element)
    outlist.append(triplet[keymax])
    sortedTopFive.append(outlist)
print("done another")

with open("output.txt", 'a') as outputFile:
    outputFile.write("OUTPUT B\n")   
    for list in sortedTopFive:
        outstr = ''
        outstr = " ".join([str(elem) for elem in list])
        outstr += "\n"
        outputFile.write(outstr)

# Algorithm's stop point:
print("All done")
