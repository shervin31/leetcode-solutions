class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        # Create a dummy node pointing to the head
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr is not None:
            if curr.val == val:
                # Skip the node by pointing prev to the node after curr
                prev.next = curr.next
            else:
                # Only move prev forward if we didn't delete curr
                prev = curr
            
            # Always move curr forward
            curr = curr.next
            
        # Return whatever is after our dummy node as the new head
        return dummy.next