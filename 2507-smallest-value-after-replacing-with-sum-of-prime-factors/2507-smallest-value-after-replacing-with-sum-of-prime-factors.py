class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            total_sum = 0
            temp = n
            d = 2
            while d * d <= temp:
                while temp % d == 0:
                    total_sum += d
                    temp //= d
                d += 1
            if temp > 1:
                total_sum += temp
            if total_sum == n:
                return n
            n = total_sum