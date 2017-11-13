def memoization(f):
    cache = {}
    def helper(n,m):
        if (n,m) not in cache:            
            cache[(n,m)] = f(n,m)
        return cache[(n,m)]
    return helper

@memoization
def p(n, m):
    if (n == 0 or m == 1):
        return 1
    if (m == 0 or n < 0):
        return 0
    if n == m:
        return 1 + p(n, m - 1)    

    return p(n, m - 1) + p(n - m, m)

def exp_sum(n):
    return(p(n,n))


#### Smart solution
    
    
    
def exp_sum1(n):
  if n < 0:
    return 0
  dp = [1]+[0]*n
  for num in xrange(1,n+1):
    for i in xrange(num,n+1):
      dp[i] += dp[i-num]
  return dp[-1]