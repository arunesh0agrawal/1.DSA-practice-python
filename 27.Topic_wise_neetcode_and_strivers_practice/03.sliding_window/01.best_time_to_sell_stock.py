# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# optimized method [ T(n) : O(n)]
def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        # Update minimum price if the current price is lower
        min_price = min(min_price, price)

        # Calculate profit by selling at the current price
        current_profit = price - min_price

        # Update maximum profit if the current profit is higher
        max_profit = max(max_profit, current_profit)

    return max_profit

# Example usage:
stock_prices = [7, 1, 5, 3, 6, 4]
result = max_profit(stock_prices)
print(result)



# sliding window style( very slow method) : [ T(n) : O(n2)]
# def maxProfit(prices: list[int]) -> int:
#         maxVal = 0
#         first, second = 0, 1
#         for i in range(len(prices)-1):
#             while second < len(prices) and prices[second] - prices[first] > 0:
#                 maxVal = max(maxVal, prices[second] - prices[first])
#                 second += 1
#             first += 1
#             second = first + 1
            
#         return maxVal

# stock_prices = [7, 1, 5, 3, 6, 4]
# result = maxProfit(stock_prices)
# print(result)