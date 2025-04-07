from typing import *
from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        line = [-1] * 100001
        zero = []
        one = []
        for winner, loster in matches:
            if line[winner] == -1:
                line[winner] = 0
            if line[loster] == -1:
                line[loster] = 1
            else:
                line[loster] += 1
        for i in range(100001):
            if line[i] == 0:
                zero.append(i)
            if line[i] == 1:
                one.append(i)
        return [zero, one]
# leetcode submit region end(Prohibit modification and deletion)
