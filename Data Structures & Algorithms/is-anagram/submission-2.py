class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dics = {}
        dicz ={}
        for i ,char in enumerate(s) :
            if char in dics :
                dics[char] +=1 
            else : dics[char] = 1
        for i , char in enumerate (t) :
            if char in dicz : 
                dicz[char] +=1 
            else : dicz[char] = 1
        if dicz == dics :
            return True
        else : return False

