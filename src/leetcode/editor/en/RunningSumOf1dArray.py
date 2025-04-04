from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        return prefix
# leetcode submit region end(Prohibit modification and deletion)
