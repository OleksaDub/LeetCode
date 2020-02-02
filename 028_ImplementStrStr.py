#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:54:45 2020
28. Implement strStr()
@author: oleksadub
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
    
'''
Runtime: 24 ms, faster than 92.04% of Python3 online submissions 
for Implement strStr().
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions 
for Implement strStr().
'''