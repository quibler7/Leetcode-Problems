class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast slow pointer method

        fast, slow = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
            if slow == fast:
                return True
                break
        
        return False
        
        
        