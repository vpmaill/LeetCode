class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def fillListNode(listToFill):
    if len(listToFill) == 1:
        return ListNode(listToFill[0])
    else:
        return ListNode(listToFill[0], fillListNode(listToFill[1:]))


def removeNthFromEnd(head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    templist = []
    i = head
    while i != None:
        templist.append(i.val)
        i = i.next

    templist.pop(-n)
    if not templist:
        return None
    return fillListNode(templist)


print(removeNthFromEnd(fillListNode([1, 2, 3, 4, 5]), 2))
