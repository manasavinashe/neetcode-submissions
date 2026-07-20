class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int] :
       A = []
       for i , num in enumerate(nums) :
            A.append([num,i])
       A.sort()
       i = 0
       j = len(A) - 1
       while True :
        a = A[i][0] + A[j][0]
        if a == target : 
                return [min(A[i][1], A[j][1]) , max([A[i][1], A[j][1]])]
        elif a > target : 
                j -= 1 
        elif a < target : 
                i +=1 
            


            

                
        