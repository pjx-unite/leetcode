# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = curr = ans = 0
        for i in range(k):
            curr += nums[i]
        ans=curr
        # 右侧相加，减少k的数量
        for i in range(k, len(nums)):

            curr = curr - nums[i - k] + nums[i]
            ans = max(ans, curr)
        return ans / k

# leetcode submit region end(Prohibit modification and deletion)
