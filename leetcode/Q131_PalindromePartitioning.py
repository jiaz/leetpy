# -*- coding: utf-8 -*-

# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
#
# Return
#
#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]
#
#
# Link:
#     https://leetcode.com/problems/palindrome-partitioning/


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
