#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
80. Remove Duplicates from Sorted Array II
medium
Created on Sat Feb  1 21:20:32 2020
@author: oleksadub
"""

class Solution:
    def removeDuplicates(self, nums):
        nums.append(-1000)
        nums.append(-1001)
        n = 0
        while n < len(nums)-2:
            while nums[n] == nums[n+2]:
                del nums[n+2]
            n += 1
            
        del nums[-1]
        del nums[-1]
        
        return len(nums)
    
"""
Runtime: 56 ms, faster than 53.59% of Python3 online submissions 
for Remove Duplicates from Sorted Array II.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions 
for Remove Duplicates from Sorted Array II.
"""