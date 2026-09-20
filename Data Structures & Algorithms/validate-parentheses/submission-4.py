class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")" : "(" , "]" : "[" , "}" : "{"}
        stack = []

        n = len(s)

        if n%2 != 0 : 
            return False 
        else  : 
            for ch in s : 
                if ch in pairs : 
                    if stack and stack[-1] == pairs[ch] : 
                        stack.pop()
                    else : 
                        return False 
                else :
                    stack.append(ch)
                
        return not stack 
            
                    


