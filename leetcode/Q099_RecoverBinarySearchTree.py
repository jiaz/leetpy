# -*- coding: utf-8 -*-

# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
#
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
#
# OJ's Binary Tree Serialization:
#
# The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.
#
# Here's an example:
#
#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
#
# The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
#
#
# Link:
#     https://leetcode.com/problems/recover-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
