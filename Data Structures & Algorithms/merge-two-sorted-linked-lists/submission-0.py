
class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        itr1 = list1 
        while itr1 :
            list.append(itr1.val)
            itr1 = itr1.next
        itr2 = list2 
        while itr2 : 
            list.append(itr2.val)
            itr2 = itr2.next
        
        
        list.sort()
        dummy = ListNode()
        tail = dummy
        for v in list:
            tail.next = ListNode(v)
            tail = tail.next
        return dummy.next

        
        