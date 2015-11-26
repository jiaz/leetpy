# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).

# TODO: Need revisit


class Solution(object):
    def findMedian(self, nums):
        l = len(nums)
        if l % 2 == 0:
            return (nums[l / 2] + nums[l / 2 - 1]) / 2.0
        else:
            return nums[l / 2]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2

        d = len(nums1)

        if d == 0:
            return self.findMedian(nums2)
        elif d > 2:
            m1 = self.findMedian(nums1)
            m2 = self.findMedian(nums2)
            if m1 == m2:
                return m1
            elif m1 > m2:
                if d % 2 == 0:
                    r = d / 2 - 1
                else:
                    r = d / 2
                return self.findMedianSortedArrays(nums1[:-1 * r], nums2[r:])
            else:
                if d % 2 == 0:
                    r = d / 2 - 1
                else:
                    r = d / 2
                return self.findMedianSortedArrays(nums1[r:], nums2[:-1 * r])
        else:
            L = d + len(nums2)
            p1 = 0
            p2 = max(L / 2 - 1 - d, 0)
            while p1 + p2 <= L / 2:
                if p1 >= d or (p2 < len(nums2) and nums1[p1] > nums2[p2]):
                    c = nums2[p2]
                    p2 += 1
                else:
                    c = nums1[p1]
                    p1 += 1
                if L % 2 == 0:
                    if p1 + p2 == L / 2:
                        a = c
                    elif p1 + p2 == L / 2 + 1:
                        b = c
                else:
                    if p1 + p2 == L / 2 + 1:
                        a = b = c

            return (a + b) / 2.0
