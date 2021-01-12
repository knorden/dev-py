import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []


def checkOverlap(a, b):
    c = []
    for num in a and b:
        if num in a and b:
            c.append(num)

    print(c)


def randGenerateList(list):
    print()
    for i in range(0, 7):
        n = random.randint(0, 16)
        list.append(n)
    print(list)
    return list


d = []
e = []

randGenerateList(d)
# print(d)
randGenerateList(e)
# print(e)

print("\nNow we check for overlap:")
checkOverlap(d, e)
