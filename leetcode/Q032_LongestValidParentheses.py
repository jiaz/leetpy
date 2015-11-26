# -*- coding: utf-8 -*-

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
#
#
# Link:
#     https://leetcode.com/problems/longest-valid-parentheses/


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
