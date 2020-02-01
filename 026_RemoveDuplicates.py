#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
26. Remove Duplicates from Sorted Array
Created on Sat Feb  1 20:29:12 2020
@author: oleksadub
"""

class Solution:
    def removeDuplicates(self, nums):
        nums.append(-1000)
        n = 0
        while n < len(nums)-1:
            while nums[n] == nums[n+1]:
                del nums[n+1]
            n += 1
            
        del nums[-1]
        
        return len(nums)
    
"""
Runtime: 88 ms, faster than 59.31% of Python3 online submissions for 
Remove Duplicates from Sorted Array.
Memory Usage: 14.4 MB, less than 99.18% of Python3 online submissions for 
Remove Duplicates from Sorted Array.
"""