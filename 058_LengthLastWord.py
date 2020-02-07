#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 23:29:10 2020
58. Length of Last Word
@author: oleksadub
"""

def lengthOfLastWord(s: str) -> int:
    s = s.strip()
    if len(s) == 0:
        return 0
    elif s.rfind(' ') == -1:
        return len(s)
    else:
        return len(s[s.rfind(' ')+1:])

'''
Runtime: 28 ms, faster than 60.91% of Python3 online submissions 
for Length of Last Word.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions 
for Length of Last Word.
'''