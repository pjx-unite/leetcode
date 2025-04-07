from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)
        for i in range(len(nums)+1):
            if i not in s:
                return i

# leetcode submit region end(Prohibit modification and deletion)
