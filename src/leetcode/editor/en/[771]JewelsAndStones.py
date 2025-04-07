from typing import *
from collections import *
from collections import Counter

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #宝石
        s=set(jewels)
        return sum([i in s for i in stones])

# leetcode submit region end(Prohibit modification and deletion)
