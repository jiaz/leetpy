# -*- coding: utf-8 -*-

# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#
#
# Link:
#     https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
