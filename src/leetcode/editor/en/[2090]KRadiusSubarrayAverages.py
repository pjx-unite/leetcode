from sys import prefix
from typing import *
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        #
        left=curr=ans=0
        ans=[]
        if 2*k>len(nums):return [-1]*len(nums);
        #求出前坠和，使用前缀和的相减来计算总和i-j prefix[j]-prefix[i-1]
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[-1])
        #遍历，看k值的半径是否符合条件
        for i in range(len(nums)):
            if i-k>=0 and i+k<len(nums):
                if i-k==0:
                    ans.append((prefix[i+k])//(2*k+1))
                else:
                    ans.append((prefix[i+k]-prefix[i-k-1])//(2*k+1))
            else:
                ans.append(-1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
