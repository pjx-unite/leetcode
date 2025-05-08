from typing import *
from collections import deque
from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)
class MovingAverage:

    def __init__(self, size: int):
        self.deque = deque(maxlen=size)

    def next(self, val: int) -> float:
        self.deque.append(val)
        return sum(self.deque) / len(self.deque)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# leetcode submit region end(Prohibit modification and deletion)