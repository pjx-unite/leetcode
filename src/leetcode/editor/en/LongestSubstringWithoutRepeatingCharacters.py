# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        chars = {}
        i = 0
        res = 0
        for j in range(n):
            if s[j] in chars:
                i = max(i, chars[s[j]])
            res = max(res, j - i + 1)
            chars[s[j]] = j + 1
        return res
        pass
# leetcode submit region end(Prohibit modification and deletion)
