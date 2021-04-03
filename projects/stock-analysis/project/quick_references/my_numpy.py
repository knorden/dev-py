import numpy as np
import pandas as pd
import cython
# from Cython import cdef


# aa = np.ones((5,10))
# bb = np.random.rand(5,10)

# def myCurryingFunc(v,fn):
    # def curryHelper(x):
        # return fn(v,x)
    # return curryHelper

# ff = [[1,2],[],[3,4,5]]
# gg = (list(map(myCurryingFunc(0, lambda v,L: L+[v]), ff)))


df = pd.DataFrame(
    {
        "a": np.random.randn(1000),
        "b": np.random.randn(1000),
        "N": np.random.randint(100, 1000, (1000)),
        "x": "x",
    }
)


# Pure Python
def f(x):
    return x * (x - 1)


def integrate_f(a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a + i*dx)
    return s*dx


# Cython
#! Cython
def f_plain(x):
    return x * (x -1)


def integrate_f_plain(a,b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f_plain(a + i*dx)
    return s*dx


