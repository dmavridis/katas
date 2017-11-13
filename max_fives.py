def solution(digits):
    '''
    return largest five digit number of a long number
    '''
   
    fives = [int(digits[i:(i+5)]) for i in range(len(digits)-4)]
    
    return max(fives)