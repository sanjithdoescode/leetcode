'''
Day - 6
Problem - 1769
Minimum Number of Operations to Move All Balls to Each Box

You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.
'''

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        ans=[0]*n
        P=[]

        for i, x in enumerate(boxes):
            if x=='1':
                P.append(i)
                ans[0]+=i

        pz=len(P)
        L, R=0, pz
        j=0
        for i in range(1, n):
            if j<pz and i>P[j]:
                L+=1
                R-=1
                j+=1
            ans[i]=ans[i-1]+L-R
        return ans
