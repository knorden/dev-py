from numpy import floor


def inc_recur(x):
    if x == 0:
        return 1
    else:
        if x % 2 == 1:
            y = int(floor(x/2))
            y = 2 * inc_recur(y)
            return y
        else:
            return x + 1


def inc_reccur2(x):
    if x == 0:
        return 1
    else:
        return 2*inc_reccur2(floor(x/2)) if x % 2 == 1 else x + 1

def inc(x):
    return x + 1

print(inc_recur(5))
print(inc_reccur2(5))
