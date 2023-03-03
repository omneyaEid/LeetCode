from typing import List


# float('inf') It acts as an unbounded upper value for comparison.
# This is useful for finding lowest values for something.
# for example,
# calculating path route costs when traversing trees.
class Solution:
    @staticmethod
    def max_profit(prices: List[int]) -> int:
        max_profit = 0
        min_buy = float('inf')
        for price in prices:
            min_buy = min(min_buy, price)
            max_profit = max(max_profit, price - min_buy)
        return max_profit


calling_class = Solution()

result = calling_class.max_profit([7, 1, 5, 3, 6, 4])
print(result)
