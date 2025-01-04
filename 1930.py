'''
Day - 4 
Problem - 1930
Unique Length - 3 Palindromic Subsequences
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
'''

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [float('inf')] * 26
        last = [-1] * 26
        result = 0

        for i, char in enumerate(s):
            first[ord(char) - ord('a')] = min(first[ord(char) - ord('a')], i)
            last[ord(char) - ord('a')] = i

        for i in range(26):
            if first[i] < last[i]:
                result += len(set(s[first[i] + 1:last[i]]))

        return result
