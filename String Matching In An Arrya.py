'''
Day - 7
Problem - 1408
String Matching In An Array

Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string
'''

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for index_1 in range(len(words)):
            for index_2 in range(len(words)):
                if index_1 != index_2 and words[index_1] in words[index_2]:
                    result.append(words[index_1])
                    break
        return result
