def fib(n):
    if n < 3:
       return n
    else:
       ans = fib(n - 2) + fib(n - 1)
       print(f"{ans} \n")
    return ans

fib(int(input()))
