# BestTimeToBuyAndSellStock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        to_buy = prices[0]
        to_sell = prices[0]
        flag = False

        for p in prices:
            if p < to_buy:
                to_buy = p
                flag = True
            else:
                if flag or p > to_sell:
                    profit = p - to_buy
                    if max_profit < profit:
                        max_profit = profit
                        to_sell = p
                        flag = False

        return max_profit


'''
Runtime: 920 ms, faster than 98.02 % of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.1 MB, less than 82.60 % of Python3 online submissions for Best Time to Buy and Sell Stock.
'''
