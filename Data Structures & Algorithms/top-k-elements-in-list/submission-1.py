class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for i in range(len(nums) + 1 )]
        for num in nums : 
            counter[num] = 1 + counter.get(num, 0)
        for n, c in counter.items() :
            freq[c].append(n)
        result = []
        for i in range(len(nums) , 0 , -1 ) : 
            for x in freq[i] : 
                result.append(x)
            if len(result) == k :
                return result

