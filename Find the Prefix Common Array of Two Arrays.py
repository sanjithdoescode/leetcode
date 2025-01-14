'''
Day - 14
Problem - 2657
Find the Prefix Common Array of Two Arrays

You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
'''

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result = [0] * n
        count = [0] * (n + 1)
        common = 0
        
        for i in range(n):
            count[A[i]] += 1
            if count[A[i]] == 2:
                common += 1
            count[B[i]] += 1
            if count[B[i]] == 2:
                common += 1
            result[i] = common
        return result
