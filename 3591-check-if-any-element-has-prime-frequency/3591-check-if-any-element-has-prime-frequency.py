from collections import Counter
from typing import List
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        counts = Counter(nums)
        return any(freq in primes for freq in counts.values())