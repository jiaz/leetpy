# -*- coding: utf-8 -*-

# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
#
#
# Link:
#     https://leetcode.com/problems/palindrome-partitioning-ii/


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
