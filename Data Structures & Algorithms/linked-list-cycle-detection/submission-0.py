
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        itr = head 
        while itr : 
            if itr in seen : 
                return True 
            seen.add(itr) 
            itr = itr.next 

        return False
    

        