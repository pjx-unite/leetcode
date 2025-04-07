from typing import *
from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        frequency_map=Counter(nums)
        return max((num for num,freq in frequency_map.items() if freq==1),default=-1)
        #time:O(n)
        #space:O(n)
# leetcode submit region end(Prohibit modification and deletion)
