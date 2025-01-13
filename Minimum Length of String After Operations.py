'''
Day - 13
Problem - 3223
Minimum Length of String After Operations

You are given a string s.

You can perform the following process on s any number of times:

Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
Delete the closest character to the left of index i that is equal to s[i].
Delete the closest character to the right of index i that is equal to s[i].
Return the minimum length of the final string s that you can achieve.
'''

class Solution:
    def minimumLength(self, s: str) -> int:
        char_frequency = [0] * 26
        total_length = 0
        for char in s:
            char_frequency[ord(char) - ord('a')] += 1
        for frequency in char_frequency:
            if frequency == 0:
                continue
            if frequency % 2 == 0:
                total_length += 2
            else:
                total_length += 1
        return total_length
