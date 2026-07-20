class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = nums
        for i in range (len(nums)):
            a = target - nums[i]
            if a in hashmap :
              b = hashmap.index(a)
              if b != i : 
                return sorted([i, b])
        return -1 

                
        