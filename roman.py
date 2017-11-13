def digits(n):
    '''yields the digits of the number'''
    counts = [1000, 100, 10, 1]
    digits = []
    for i,count in enumerate(counts):
        div, rem = divmod(n, count)
        digits.append(div)
        n = rem
    return digits
    

def solution(n):
    romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    romans = romans[::-1]
    counts = [1000, 500, 100, 50, 10, 5, 1]
    
    # TODO convert int to roman string
    roman = ''
    digit = digits(n)
    print(digit)
    for i,d in enumerate(digit):
        if d in [1,2,3]:
            roman += (d*romans[2*i])
        elif d in [4]:
            roman += (romans[2*i] + romans[2*i-1])
        elif d in [5]:
            roman += (romans[2*i-1])
        elif d in [6,7,8]:
            roman += (romans[2*i-1] + (d-5)*romans[2*i])
        elif d in [9]:
            roman += (romans[2*i] + romans[2*i-2])
    return roman


'''
def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string

'''