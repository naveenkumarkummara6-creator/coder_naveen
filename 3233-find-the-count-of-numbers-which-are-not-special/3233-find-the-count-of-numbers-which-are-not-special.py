import math
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        limit = math.isqrt(r)
        def is_prime(n):
            if n < 2: return False
            for i in range(2, math.isqrt(n) + 1):
                if n % i == 0: return False
            return True
        special = 0
        for p in range(2, limit + 1):
            if is_prime(p) and l <= p * p <= r:
                special += 1
        return (r - l + 1) - special