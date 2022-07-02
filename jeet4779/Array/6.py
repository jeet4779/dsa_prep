'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

'''
Explaination: Simple dp question and mostly asked, two variables prevmin will store the previous min we just encountered and ans will store the profit if we would have
bought the stock on the previous day and selling it today. If prevmin is the current element, we will get 0, which ovbiously makes sense.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevmin = 999999
        ans = -1
        for i in range(len(prices)):
            prevmin= min(prevmin,prices[i])
            ans = max(prices[i]-prevmin, ans )
        return ans
