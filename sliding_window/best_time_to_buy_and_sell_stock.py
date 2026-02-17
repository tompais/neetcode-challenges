from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price with the first element
        min_price = prices[0]
        # Initialize the maximum profit to 0
        max_profit = 0
        # Iterate from the second price onwards
        for price in prices[1:]:
            # Update min_price if a lower price is found
            if price < min_price:
                min_price = price
            # Update max_profit if the profit from selling at the current price is higher
            elif price - min_price > max_profit:
                max_profit = price - min_price
        # Return the maximum profit found
        return max_profit
