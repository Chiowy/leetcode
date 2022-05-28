"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] 
if and only if either (a == c and b == d), or (a == d and b == c) - that is, 
one domino can be rotated to be equal to another domino.
Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
"""

from typing import List # 解决NameError: name 'List' is not defined
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        """ 
        NumberOfPairs = 0
        for head in range(len(dominoes)):
            tail = len(dominoes) - 1
            while head < tail:
                if (dominoes[head][0] == dominoes[tail][0] and dominoes[head][1] == dominoes[tail][1]) or (dominoes[head][0] == dominoes[tail][1] and dominoes[head][1] == dominoes[tail][0]):
                    NumberOfPairs += 1
                tail -= 1
        return NumberOfPairs """

        # step 1: count the dominoes
        d = {}
        for domi in dominoes:
            p = tuple(sorted(domi))
            if p in d:
                d[p] += 1
            else:
                d[p] = 1
        # step 2: caculate the pairs. for each pair, number of pairs = n*(n-1)//2
        c = 0
        for n in d.values():
            s = n*(n-1)//2
            c += s
        return c




print(Solution().numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))

