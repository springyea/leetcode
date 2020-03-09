from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        min_price = inf
        max_profit = 0
        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    assert(Solution().maxProfit(prices) == 5)
    prices = [7, 6, 4, 3, 1]
    assert(Solution().maxProfit(prices) == 0)
