# -*- coding: utf-8 -*-

# Given a collection of integers that might contain duplicates, nums, return all possible subsets.
#
# Note:
#
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,2], a solution is:
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#
#
# Link:
#     https://leetcode.com/problems/subsets-ii/


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
