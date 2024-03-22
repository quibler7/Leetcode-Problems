class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return True

        def reverse(head):
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        slow = reverse(slow)
        fast = head

        while slow:

            if slow.val != fast.val: return False
            slow = slow.next
            fast = fast.next

        return True





