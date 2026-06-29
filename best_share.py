class Solution:
    def maxProfit(self, prices):
        lowest_price = prices[0]
        max_profit = 0

        for price in prices:

            if price < lowest_price:
                # update lowest_price
                lowest_price = price

            current_profit = price - lowest_price

            if current_profit > max_profit:
                # update max_profit
                max_profit = current_profit

        return max_profit
    

solution = Solution()

print(solution.maxProfit(prices = [7,1,5,3,6,4]))