class RomanNumerals():
    romans = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 
              'X':10, 'XL': 40, 'L': 50, 'XC': 90, 
              'C': 100, 'CD':400, 'D':500, 'CM': 900,
              'M':1000}
    nums = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 
            10:'X', 40:'XL', 50:'L', 90: 'XC', 
            100:'C', 400: 'CD', 500:'D', 900: 'CM',
            1000:'M'}

    @classmethod
    def __init__(self):
        pass
    
    def to_roman(self, num):
        # convert the numbers to roman base number
        roman = []
        for ii in reversed(sorted(self.nums.keys())):            
            div, num = divmod(num,ii)
            roman += div*self.nums[ii]
        return ''.join(roman)
 
    @classmethod
    def from_roman(self, roman_num):
        'Check for two numbbers'
        num = 0
        pairs = [roman_num[i:i+2] for i in range(0, len(roman_num), 1)]
        for el in pairs:
            if el in self.romans.keys() and len(el) == 2:
                num += self.romans[el]
                roman_num = roman_num.replace(el, '')
        
        for el in roman_num:
            num += self.romans[el]
        return num

r= RomanNumerals()
print(r.from_roman('VII'))
print(r.to_roman(7))