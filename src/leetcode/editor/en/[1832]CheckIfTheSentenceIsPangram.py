from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=set()
        for c in sentence:
            s.add(c)
        return len(s)==26
# leetcode submit region end(Prohibit modification and deletion)
