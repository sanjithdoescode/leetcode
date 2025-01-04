'''
Day - 4
Problem - 4
Median Of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n2 = len(nums2)
        for i in range(n2):
            nums1.append(nums2[i])

        nums1.sort()
        n1 = len(nums1)
        if n1 % 2 != 0:
            res = float(nums1[n1 // 2])  
            return res
        else:
            mid = n1 // 2  
            res = (nums1[mid - 1] + nums1[mid]) / 2  
            res = float(res)  
            return res
