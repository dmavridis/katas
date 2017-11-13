import math

def calculate_sums(x, k):
    '''
    n: number to break into sum of squares
    k: max power for adding number
    '''
    base = [ii for ii in range(k,0,-1)]    
    squares = [ii**2 for ii in range(k,0,-1)]
    
    
    if sum(squares[ii] for ii in range(k)) < x:
        return None
    
    for res in range(2**k-1,0,-1):
        bin_res = format(res, 'b').zfill(k)
        if sum(squares[ii]*int(bin_res[ii]) for ii in range(k)) == x:
            return sorted([base[jj] for jj in range(k) if bin_res[jj] != '0'])
        elif sum(squares[ii]*int(bin_res[ii]) for ii in range(k)) < x:
            return None 
#    return None  
        
def decompose(n):
    # result after first step
    x = 2*n-1
    k = int(math.sqrt(x))
    
    sub_result = None
    while (sub_result is None and k>1):
#        print(x,k)
        sub_result = calculate_sums(x, k)
        k -= 1    
    return sub_result + [n-1] if sub_result is not None else None

print(calculate_sums(105,8))

#
#print(11, decompose(11))
#print(50, decompose(50))
#print(5, decompose(5))
#print(44, decompose(44))
#
#k = 4
#squares = [ii**2 for ii in range(k,0,-1)]
#for res in range(2**k-1,0,-1):
#    bin_res = format(res, 'b').zfill(k)
#    print(res, bin_res, sum(squares[ii]*int(bin_res[ii]) for ii in range(k)))