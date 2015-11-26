# -*- coding: utf-8 -*-

# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
#
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Return
#
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
#
# Note:
#
# All words have the same length.
# All words contain only lowercase alphabetic characters.
#
#
# Link:
#     https://leetcode.com/problems/word-ladder-ii/


class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        
