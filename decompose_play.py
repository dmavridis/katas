import math

def calculate_sums(x, k):
    '''
    n: number to break into sum of squares
    k: max power for adding number
    '''
    
    base = [k for k in range(k,0,-1)]
    
    res = []
    for k in base:
        print(x)
        div, x = divmod(x, k**2)
#        print(k,x, div)
        if div > 1:
            return None
        elif div == 1:
           res.append(k**2) 
            
    
    return res  



def decompose(n):
    # result after first step
    x = 2*n-1
    k = int(math.sqrt(x))
    
    sub_result = None
    while (sub_result is None and k>1):
        sub_result = calculate_sums(x, k)
        k -= 1    
    return sub_result

print(calculate_sums(87,6))

#print(11, decompose(11))
#print(50, decompose(50))
#print(5, decompose(5))
#print(44, decompose(44))