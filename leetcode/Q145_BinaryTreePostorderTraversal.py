# -*- coding: utf-8 -*-

# Given a binary tree, return the postorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#
#    1
#     \
#      2
#     /
#    3
#
# return [3,2,1].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#
# Link:
#     https://leetcode.com/problems/binary-tree-postorder-traversal/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
