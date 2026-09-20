class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for i in s : 
            dic1[i] = dic1.get( i , 0) + 1 
        for j in t : 
            dic2[j] = dic2.get(j , 0) + 1 
        
        if dic1 == dic2 : 
            for i in dic1 : 
                if dic2[i] != dic1[i] : 
                    return False
            return True
        else : return False 


        