from typing import *
from collections import *
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1=defaultdict(int)
        dict2=defaultdict(int)
        for i in ransomNote:
            dict1[i]+=1
        for i in magazine:
            dict2[i]+=1
        #这里不能遍历dict2，因为dict1内的字母有可能没在dict2中，是从dict1中遍历所有的字母
        for key in dict1:
            if dict1[key]<=dict2[key]:
                continue
            else:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
