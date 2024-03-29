# -*- coding: utf-8 -*-

# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# Ensure that numbers within the set are sorted in ascending order.
#
#  Example 1:
# Input:  k = 3,  n = 7
# Output:
#
# [[1,2,4]]
#
#  Example 2:
# Input:  k = 3,  n = 9
# Output:
#
# [[1,2,6], [1,3,5], [2,3,4]]
#
# Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.
#
# Link:
#     https://leetcode.com/problems/combination-sum-iii/


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
