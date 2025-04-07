from typing import *
from collections import *
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        frequency_map= defaultdict(int)
        for chat in text:
            frequency_map[chat]+=1
        one=two=0
        if frequency_map['l']<frequency_map['o']:
            two=frequency_map['l']
        else:
            two=frequency_map['o']
        one=min(frequency_map['b'],frequency_map['a'],frequency_map['n'])
        if one*2>two:
            return two//2
        else:
            return one

# leetcode submit region end(Prohibit modification and deletion)
