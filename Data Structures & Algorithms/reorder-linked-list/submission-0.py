# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = None
        slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        l = head
        r = prev
        while r:
            nxt_f = l.next
            nxt_b = r.next
            l.next = r
            r.next =nxt_f
            l = nxt_f
            r = nxt_b



        

        