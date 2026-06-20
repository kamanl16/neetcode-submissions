class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        head_ptr = 0
        tail_ptr = 1
        profit = 0

        while tail_ptr < len(prices):
            profit = max(profit, prices[tail_ptr] - prices[head_ptr])

            if prices[head_ptr] > prices[tail_ptr]:
                head_ptr = tail_ptr
                tail_ptr += 1
            else:
                tail_ptr += 1
        
        return profit
        