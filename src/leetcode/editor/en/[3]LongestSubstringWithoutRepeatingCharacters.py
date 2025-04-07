from typing import *
from collections import *
from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left  = ans = 0
        dict = defaultdict(int)
        for right in range(len(s)):
            if s[right] in dict:
                left = max(left, dict[s[right]])
            ans = max(ans, right - left + 1)
            dict[s[right]] = right + 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
