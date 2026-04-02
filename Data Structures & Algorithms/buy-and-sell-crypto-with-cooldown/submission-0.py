class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [buy, sell, cooldown]
        m = 0
        def profit(i, state, prices, p, m):
            if i == len(prices):
                return max(m ,p)
            if state == 0:
                return max(profit(i+1, 1, prices, p-prices[i],m), profit(i+1, 0, prices, p,m))
            elif state==1:
                return max(profit(i+1, 2, prices, p+prices[i],m), profit(i+1, 1, prices, p,m))
            else:
                return profit(i+1, 0, prices, p, m)
        return profit(0, 0 ,prices, 0, 0)
                