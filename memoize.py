# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 08:01:38 2016

@author: Dimitrios
"""

factorial_memo = {}

def factorial(k):
    
    if k < 2: 
        return 1
    
    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
        
    return factorial_memo[k]
    
memo = {}

