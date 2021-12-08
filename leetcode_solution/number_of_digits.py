class Solution:
    def countDigitOne(self, n: int) -> int:
        res = 0
        cur = 1
        while cur <= n:
            res += ((n // (cur * 10)) * cur) + min(
                max(n % (cur * 10) - cur + 1, 0), cur
            )

            cur *= 10

        return res
