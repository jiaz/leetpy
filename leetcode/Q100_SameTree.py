# -*- coding: utf-8 -*-

# Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
#
#
# Link:
#     https://leetcode.com/problems/same-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
