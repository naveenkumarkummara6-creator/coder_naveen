class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        n = len(nums)
        max_prime = 0
        for i in range(n):
            val1 = nums[i][i]
            if val1 > max_prime and is_prime(val1):
                max_prime = val1
            val2 = nums[i][n - i - 1]
            if val2 > max_prime and is_prime(val2):
                max_prime = val2
        return max_prime