class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums : 
            if num in dic :
                dic[num] += 1
            else : dic[num] = 1 

        result = []
        for x in range(k) : 
            best_i , best_v = None, float('-inf')
            for i, v in dic.items() :
                if v > best_v :
                    best_i, best_v = i, v 
            del dic[best_i]
            result.append(best_i)
        return result


        