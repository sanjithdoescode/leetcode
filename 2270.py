'''
Day - 3
Problem - 2270 (POTD)
Number Of Ways To Split Array

You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.
'''
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        length = len(nums)
        result = 0

        # Step 1: Calculate prefix sum
        prefix = [0] * length
        prefix[0] = nums[0]
        for i in range(1, length):
            prefix[i] = nums[i] + prefix[i - 1]

        # Step 2: Calculate total sum
        total_sum = prefix[-1]

        # Step 3: Iterate through split points and check conditions
        for i in range(length - 1):
            if prefix[i] >= (total_sum - prefix[i]):
                result += 1

        return result
