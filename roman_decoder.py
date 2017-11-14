def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    romans = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 
              'X':10, 'XL': 40, 'L': 50, 'XC': 90, 
              'C': 100, 'CD':400, 'D':500, 'CM': 900,
              'M':1000}
  
    num = 0
    pairs = [roman[i:i+2] for i in range(0, len(roman), 1)]

    for el in pairs:
        if el in romans.keys() and len(el)==2:
            num += romans[el]
            roman = roman.replace(el, '')
    for el in roman:
        num += romans[el]
    return num

print(solution('IV'))