def memoization(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoization
def fib(n):
    if n in [0, 1, -1]:
        return abs(n)
    elif n > 1: 
        return fib(n - 1) + fib(n - 2)
    else:
        return fib(n + 2) - fib(n + 1)
        