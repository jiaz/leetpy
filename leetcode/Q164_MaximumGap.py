# -*- coding: utf-8 -*-

# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#
# Try to solve it in linear time/space.
#
# Return 0 if the array contains less than 2 elements.
#
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
#
# Credits:Special thanks to @porker2008 for adding this problem and creating all test cases.
#
# Link:
#     https://leetcode.com/problems/maximum-gap/


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
