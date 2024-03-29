# -*- coding: utf-8 -*-

# Compare two version numbers version1 and version2.
# If version1 &gt; version2 return 1, if version1 &lt; version2 return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
#
# Here is an example of version numbers ordering:
# 0.1 &lt; 1.1 &lt; 1.2 &lt; 13.37
#
# Credits:Special thanks to @ts for adding this problem and creating all test cases.
#
# Link:
#     https://leetcode.com/problems/compare-version-numbers/


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
