class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1) : 
            return False 
        l = 0
        hass1 = {}

        for i in s1 :
            hass1[i] = 1 + hass1.get(i, 0 )


        for r in range (len(s1) - 1, len(s2)) : 
            hass2 = {}
            for j in range (l , r +1) :
                if s2[j] in hass1 : 
                    hass2[s2[j]] = 1 + hass2.get(s2[j], 0 )
            if hass1 == hass2 : 
                return True
            else : 
                l +=1 
            
        return False 


        