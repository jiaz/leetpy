# -*- coding: utf-8 -*-

# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#
# Credits:Special thanks to @ifanchu for adding this problem and creating all test cases.
#
# Link:
#     https://leetcode.com/problems/excel-sheet-column-title/


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
