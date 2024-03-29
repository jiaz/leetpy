# -*- coding: utf-8 -*-

# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
#
# X X X X
# X O O X
# X X O X
# X O X X
#
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# Link:
#     https://leetcode.com/problems/surrounded-regions/


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
