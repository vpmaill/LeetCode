class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if l1.next == None and l2.next == None:
            if l1.val + l2.val >= 10:
                return ListNode((l1.val + l2.val) % 10, ListNode(1))
            else:
                return ListNode(l1.val + l2.val)
        else:
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            if l1.val + l2.val >= 10:
                l1.next.val += 1
            return ListNode((l1.val + l2.val) % 10, Solution.addTwoNumbers(self, l1.next, l2.next))

