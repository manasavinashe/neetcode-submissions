class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 1 :
            return 0
        
        l = 0
        r = 1 
        tillnow = 0 
        while r < n : 
            if prices[r] > prices [l] : 
                profit = prices[r] - prices[l]
                tillnow = max(tillnow, profit)
            else : 
                l = r        
            r += 1 

        if tillnow < 0 :
            return 0
        else : return tillnow 
            
            
            