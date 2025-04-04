# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        l, r = 0, len(nums) - 1
        length = len(nums)

        for i in range(length-1,-1,-1):

            if abs(nums[l]) < abs(nums[r]):
                res[length - 1] = nums[r] ** 2
                r -= 1
            else:
                res[length - 1] = nums[l] ** 2
                l += 1
            length -= 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
