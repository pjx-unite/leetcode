# leetcode submit region begin(Prohibit modification and deletion)


class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        HALF_NIN_INT = -2 ** 30
        if dividend == MIN_INT and divisor == -1: return MAX_INT
        quotient = 0
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        while divisor >= dividend:
            powOfTwo = -1
            value = divisor
            while value >= HALF_NIN_INT and value + value >= dividend:
                value += value
                powOfTwo += powOfTwo
            quotient += powOfTwo
            dividend -= value
        if negatives != 1: quotient = -quotient
        return quotient
        pass
# leetcode submit region end(Prohibit modification and deletion)
