from typing import *
from collections import *
from collections import Counter


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.

class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        if not head:
            return None

        left, right = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            if n ==1:
                return

            right = right.next

            if m > 1:
                left = left.next
            recurseAndReverse(right, m - 1, n -1)

            if left == right or right.next == left:
                stop = True
            if not stop:
                left.val, right.val = right.val, left.val

                left = left.next
        recurseAndReverse(right, m, n)
        return head




# leetcode submit region end(Prohibit modification and deletion)
