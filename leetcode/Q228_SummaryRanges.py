# -*- coding: utf-8 -*-

# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
#
# Link:
#     https://leetcode.com/problems/summary-ranges/


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
