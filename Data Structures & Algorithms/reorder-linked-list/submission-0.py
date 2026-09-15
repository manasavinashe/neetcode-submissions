
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodelist = []
        test = head
        while test:
            nodelist.append(test)
            test = test.next

        l, r = 0 , len(nodelist) - 1 
        
        while l < r : 
            nodelist[l].next = nodelist[r]
            l+=1
            if l == r : 
                break 
            nodelist[r].next = nodelist[l]
            r -=1 
        nodelist[l].next = None

            

    
     



        