'''
Day - 16
Problem - 2425
Bitwise XOR of All Pairings

You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3.
'''
from collections import defaultdict

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        freq = defaultdict(int)
        for n in nums1:
            freq[n] += n2
        for n in nums2:
            freq[n] += n1
        res = 0
        for n, c in freq.items():
            if c % 2 == 1:
                res ^= n
        return res
