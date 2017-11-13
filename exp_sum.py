'''
f(s, n) = 1                                    if s = 0
        = 0                                    if s != 0 and n = 0
        = sum f(s - i, n - 1) over i in [0, s] otherwise
'''


def f(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sum(f(i) for i in range(n))







def exp_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return(exp_sum(n-1) + exp_sum(n-2) + 1)
    
    
    
' print(exp_sum(3))'
print(f(3))