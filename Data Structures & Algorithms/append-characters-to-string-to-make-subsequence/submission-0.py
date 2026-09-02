class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        missing= []
        for ch in s :
            if i < len(t) and t[i] == ch : 
                i +=1
        if i == len(t) :
            return 0
        
        for j in range( i, len(t)) : 
            missing.append(t[j])

        return len(missing)