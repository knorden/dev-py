# tail recursion practice on the Fibonacci sequence

# def fibo(i, prev, curr, buf):
    # if i == 0:
        # return buf
    # else:
        # return fibo(i-1, curr, prev+curr, prev+curr)


# def fib(n):
    # return fibo(n, 0, 1, 0)

def fibo(i, pre, cur):
    print("{}\t: {}".format(i,pre))
    if i == 0:
        return pre
    return fibo(i-1, cur, pre+cur)

def fib(n):
    return fibo(n, 0, 1)

# def fib(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fib(n-1) + fib(n-2)


aa = fib(9)
print(aa)

# 0 1 2 3 4 5 6  7  8  9 10
# 0 1 1 2 3 5 8 13 21 34 55
