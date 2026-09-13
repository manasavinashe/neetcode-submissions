class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float('inf') 
        n = len(nums)
        for i in range(0, n) : 
            for j in range (i, n) : 
                if sum(nums[i:j + 1 ]) >= target : 
                    best = min(best, j - i + 1 )
                    break 
        return best if best!= float('inf') else 0 

        