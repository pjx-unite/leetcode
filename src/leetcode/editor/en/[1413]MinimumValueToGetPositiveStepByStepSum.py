from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        return 1 - min(prefix) if min(prefix) < 0 else 1

# leetcode submit region end(Prohibit modification and deletion)
