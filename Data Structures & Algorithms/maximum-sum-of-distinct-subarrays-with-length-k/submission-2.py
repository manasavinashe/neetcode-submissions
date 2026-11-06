class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        n = len(nums)
        count = {}
        total = 0
        best = 0 
        for r in range(n) :
            count[nums[r]] = count.get(nums[r] , 0) + 1 
            total += nums[r]
            # when window becomes larger than k : 
            if r >=k :
                l = r - k
                count[nums[l]] -= 1 
                if count[nums[l]] == 0 :
                    del count[nums[l]]
                total -= nums[l]

            # when we reach size k, window is full
            if len(count) == k  and r >= k-1 :
                best = max(best, total)
        return best 


