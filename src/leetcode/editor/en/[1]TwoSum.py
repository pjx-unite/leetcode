# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):

            if target - num in d:
                return [index, d[target - num]]
            else:
                d[num] = index
        return []
        pass
# leetcode submit region end(Prohibit modification and deletion)
