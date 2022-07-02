'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.'''

'''
Explaination: This question is conceptually difficult but if we think about it more practically the solution makes more sense. What will you do if you want to make more 
profit from the stock market, ovbiously we will buy at low and sell at high and eventually we will make more transcations and won't wait. More interestingly [1,3,6] is
that's the prices, 6-1 == 3-1 + 6-3. And this is true for every such cases so simply assume we had bought at one day and next day if price is high we sell and take profit
again suppose we bought after we sell and next day if price is high we sell, else assume that we had never bought the stock on the previos day, repeat this process to get maximum profit.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        for i in range(1,len(prices)):
            
            ans += max(0,prices[i]-prices[i-1])
            
        return ans
        
