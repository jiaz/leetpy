# -*- coding: utf-8 -*-

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
# 11110110101100000000
# Answer: 1
# Example 2:
# 11000110000010000011
# Answer: 3
#
# Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.
#
# Link:
#     https://leetcode.com/problems/number-of-islands/


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
