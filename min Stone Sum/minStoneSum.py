from heapq import *
from math import floor
from typing import List


class Solution:

    @staticmethod
    def minStoneSum(piles: List[int], k: int) -> int:
        maxHeap = []
        for i in range(len(piles)):
            heappush(maxHeap, -piles[i])

        i = k
        while i > 0:
            temp = heappop(maxHeap)
            x = floor(temp / 2)
            heappush(maxHeap, x)
            i -= 1
        return -sum(maxHeap)


calling_class = Solution()
result = calling_class.minStoneSum([4, 3, 3, 7], 2)
print("total number of stones is :", result)
