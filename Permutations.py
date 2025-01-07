'''
Day - 7
Problem - 46
Permutations

Given an array nums of distinct integers, return all the possible 
permutations. 
You can return the answer in any order.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack

        result = []
        backtrack(0)
        return result
