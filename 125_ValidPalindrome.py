#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 21:43:31 2020
125. Valid Palindrome
@author: oleksadub
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True

        from re import sub
        lower_case = s.lower()
        to_check = sub('[^a-zA-Z0-9_]', '', lower_case)

        while len(to_check) > 1:
            if to_check[0] != to_check[-1]:
                return False
            else:
                to_check = to_check[1:-1]

        return True
    
'''
Runtime: 76 ms, faster than 10.90% of Python3 online submissions 
for Valid Palindrome.
Memory Usage: 14.3 MB, less than 45.24% of Python3 online submissions 
for Valid Palindrome.
'''