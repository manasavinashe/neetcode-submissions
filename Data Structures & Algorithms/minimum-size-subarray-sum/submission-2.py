class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        best = float("inf")
        n = len(nums)

        while r < n : 
            if sum(nums[l : r + 1]) < target : 
                r += 1 
            if sum(nums[l : r+1 ]) >=target :
                best = min(best, r - l + 1)
                l +=1 
        
        return best if best != float('inf') else 0 

                

            
