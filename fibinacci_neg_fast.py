# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
    n0 = abs(n)
    if n0 == 0:
        return (0, 1)
    else:
        a, b = _fib(n0 // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n0 % 2 == 0:
            res =  (c, d)
            if n < 0:
                res = ((-1)**(n0+1)*c, 0)
        else:
            res = (d, c + d)
            if n < 0:
                res = ((-1)**(n0+1)*d, 0)
        return res    

def fib(n):
    return _fib(n)[0]        
        
print(fib(-6))