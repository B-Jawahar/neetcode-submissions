class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pr=0
        left=0
        right=1
        n=len(prices)
        while right<n:
            if prices[left]>prices[right]:
                left=right
                right+=1
            else:
                tmp=0
                while right<n:
                    pr=max(pr,(prices[right]-prices[left]))
                    right+=1
                    #print(left,right,tmp)
                left+=1
                right=left+1
                #print(tmp,pr)
                #pr=max(pr,tmp)
        return pr
                
