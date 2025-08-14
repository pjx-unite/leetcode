from typing import *
from collections import *
from collections import Counter
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1

                if count >= 2:
                    nums.pop(i)
                    i -= 1
                    count -= 1
            else:
                count = 0
            i += 1
        return len(nums)
# leetcode submit region end(Prohibit modification and deletion)
