# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
#
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
#
#
# Link:
#     https://leetcode.com/problems/zigzag-conversion/


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        result = []
        for i in range(numRows):
            result.append([])

        for i in range(len(s)):
            p = i % (numRows - 1)
            q = i / (numRows - 1)
            if q % 2 == 0:
                result[p].append(s[i])
            else:
                result[numRows - 1 - p].append(s[i])

        return ''.join(map(lambda x: ''.join(x), result))
