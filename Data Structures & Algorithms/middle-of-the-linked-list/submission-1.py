
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        test = head
        count = 0 
        while test : 
            test = test.next
            count += 1 
        
        test2 = head

    
        if count%2 == 0 :
            count2 = 0  
            while count2 < count/2 : 
                test2 = test2.next 
                count2 +=1
            return test2
        else : 
            count2 = 0 
            while count2 < count//2 : 
                test2 = test2.next 
                count2 +=1 
            return test2
        


        