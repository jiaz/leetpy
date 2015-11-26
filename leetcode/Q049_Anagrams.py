# -*- coding: utf-8 -*-

# Given an array of strings, group anagrams together.
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
# Note:
#
# For the return value, each inner list's elements must follow the lexicographic order.
# All inputs will be in lower-case.
#
#
# Link:
#     https://leetcode.com/problems/anagrams/


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
