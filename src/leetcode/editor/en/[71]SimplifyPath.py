from inspect import stack
from typing import *
from collections import *
from collections import Counter
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def simplifyPath(self, path: str) -> str:
        # 便利字符串，并且顶部判断是否含有/
        path_list = path.split('/')
        stack = []
        match = {'.', '..'}
        for c in path_list:
            if c != '' and c not in match:
                stack.append(c)
            if c == '.':
                continue
            if c == '..':
                if stack:
                    stack.pop()
        return '/' + '/'.join(stack)

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution.simplifyPath(Solution, "/home/user/Documents/../Pictures"))

