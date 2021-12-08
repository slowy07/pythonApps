class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        is_prime = [True] * (n // 2)
        cnt = len(is_prime)
        for i in xrange(3, n, 2):
            if i * i >= n:
                break
            if not is_prime[i // 2]:
                continue
            for j in xrange(i * i, n, 2 * i):
                if not is_prime[j // 2]:
                    continue
                cnt -= 1
                is_prime[j // 2] = False
        return cnt
