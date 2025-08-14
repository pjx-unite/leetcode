from typing import *
from collections import *
from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 遍历nums2位了找到一个index
        dict_2 = {num: i for i, num in enumerate(nums2)}
        ans = [0] * len(nums1)
        for i, num in enumerate(nums1):
            j = dict_2[num]
            while j < len(nums2):
                if nums1[i] < nums2[j]:
                    ans[i] = nums2[j]
                    break
                else:
                    ans[i] = -1
                    j += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
