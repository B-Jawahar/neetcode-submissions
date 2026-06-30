class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pr=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                pr=max(pr,prices[j]-prices[i])
        return pr