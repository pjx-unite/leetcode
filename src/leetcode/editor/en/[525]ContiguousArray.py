from typing import *
from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        # 计算每个子数组01是否相等
        def counter(nums: List[int]) -> int:
            if Counter(nums)[0] == Counter(nums)[1]:
                return len(nums)

            else:
                return 0
        ans=[]
        #左右指针，分别遍历然后根据0 1的数量进行
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                # 子数组
                 ans.append(counter(nums[i:j + 1]))
        return max(ans)
# leetcode submit region end(Prohibit modification and deletion)
