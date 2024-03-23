# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reach mid
        # seprate two linked lists
        # reverse second half
        # add one node from first ll and first from second ll

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        # slow.next = head
        head2 = slow.next
        # sep two linked list
        slow.next = None

        # reverse second half
        prev = None
        curr = head2
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head2 = prev

        dummy = ListNode(0)

        # add nodes from head and head2

        c1, c2 = head, head2
        while c1 and c2:
            dummy.next = c1
            c1 = c1.next
            dummy = dummy.next

            dummy.next = c2
            c2 = c2.next
            dummy = dummy.next

        dummy.next = c1 or c2

        return dummy.next



