class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        left=0
        right=1

        while right<len(prices):
            l=prices[left]
            r=prices[right]
            if l>r:
                left=right
            elif l<r:
                maxProfit=max(maxProfit, r-l)
            right+=1

        return maxProfit