#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
27. Remove Element
Created on Sat Feb  1 21:09:12 2020
@author: oleksadub
"""

class Solution:
    def removeElement(self, nums, val):
        n = 0

        while n < len(nums):
            if nums[n] == val:
                del nums[n]
            else:
                n += 1
                
        return len(nums)

    
"""
Runtime: 32 ms, faster than 58.21% of Python3 online submissions 
for Remove Element.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions 
for Remove Element.
"""