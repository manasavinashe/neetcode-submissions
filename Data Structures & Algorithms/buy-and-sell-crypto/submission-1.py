class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        if n == 1 or "" : 
            return 0  

        reg = []
        j = 0
        while j < n :
            for i in range(j+1, n) : 
                profit = prices[i] - prices[j]
                reg.append(profit)
            j +=1
        
        max = reg[0]
        for i in reg : 
            if i > max :
                max = i 
        if max < 0 :
            return 0 
        return max 

        