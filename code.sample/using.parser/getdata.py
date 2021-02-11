import csv

with open('mockdata.txt', newline='') as csvfile:
    src_line = csv.reader(csvfile, delimiter=' ')
    for item in src_line:
        print(' '.join(item))


# each line read by the reader object is separated into a list of strings, delimited by a predefined
# delimiter (in this case the ' ').
