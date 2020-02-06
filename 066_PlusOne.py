#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:47:07 2020
66. Plus One
@author: oleksadub
"""

def plusOne(digits):
    def add(n):
        return (n+1) % 10
    
    last = -1
    while True:
        digits[last] = add(digits[last])
        if digits[last] > 0:
            return digits
        elif len(digits) == -last:
            digits.insert(0, 1)
            return digits
        else:
            last -= 1
            
        #return digits
        
    
print(plusOne([9, 9]))
        
