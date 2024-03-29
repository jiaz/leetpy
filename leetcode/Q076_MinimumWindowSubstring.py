# -*- coding: utf-8 -*-

# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
#
# Minimum window is "BANC".
#
# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
#
# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
#
#
# Link:
#     https://leetcode.com/problems/minimum-window-substring/


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
