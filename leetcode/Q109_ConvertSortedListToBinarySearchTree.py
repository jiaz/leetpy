# -*- coding: utf-8 -*-

# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#
# Link:
#     https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
