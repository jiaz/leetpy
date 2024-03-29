# -*- coding: utf-8 -*-

# Given a binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
#
# Return 6.
#
#
# Link:
#     https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
