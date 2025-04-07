from typing import *
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countElements(self, arr: List[int]) -> int:
        s=set()
        ans=0
        for i in arr:
            s.add(i)
        for i in arr:
            if i+1 in s:
                ans+=1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
