def triple_double(num1, num2):
    digits = '0123456789'
    triple_digits = [digit for digit in digits if 3*digit in str(num1)]
    return sum([1 for digit in triple_digits if 2*digit in str(num2)])>0
    