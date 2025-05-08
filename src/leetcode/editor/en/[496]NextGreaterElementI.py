from typing import *
from collections import *
from collections import Counter
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                max_value=-1
                if nums1[i] == nums2[j]:
                    for k in range(j+1,len(nums2)):
                        if nums2[k]>nums1[i]:
                            max_value=nums2[k]
                            break
                    ans.append(max_value)

        return ans
# leetcode submit region end(Prohibit modification and deletion)
