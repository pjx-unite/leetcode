from typing import *

from pygments.console import ansiformat


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = curr = ans = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0: k += 1 - nums[left];left += 1
        return right - left + 1
# leetcode submit region end(Prohibit modification and deletion)
