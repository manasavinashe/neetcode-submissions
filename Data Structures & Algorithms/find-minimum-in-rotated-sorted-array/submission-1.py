class Solution:
    def findMin(self, nums: List[int]) -> int: 
        l = 0
        r = len(nums)-1 

        mini = float('inf')
        while l <= r :
            mid = (l+r)//2 
            #left sorted array

            if nums[l] <= nums[mid] :
                if nums[l] < mini :
                    mini = nums[l]
                l = mid + 1  
            # right sorted array
            else : 
                if nums[mid] < mini : 
                    mini = nums[mid]
                r = mid - 1 
            
        return mini 





        