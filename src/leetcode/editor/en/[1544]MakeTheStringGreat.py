from typing import *
from collections import *
from collections import Counter
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                top = stack.pop()
                if top.isupper() and top.lower() == c or top.islower() and top.upper() == c:
                    continue
                else:
                    stack.append(top)
                    stack.append(c)
        return ''.join(stack)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(chr(ord('C')+32))
    s = Solution()
    s.makeGood("leEeetcode")