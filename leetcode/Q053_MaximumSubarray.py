# -*- coding: utf-8 -*-

# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [&#8722;2,1,&#8722;3,4,&#8722;1,2,1,&#8722;5,4],
# the contiguous subarray [4,&#8722;1,2,1] has the largest sum = 6.
#
# click to show more practice.
#
# More practice:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#
#
# Link:
#     https://leetcode.com/problems/maximum-subarray/


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
